"""Post-processing workflow for KL Master appeal status updates."""

import os
import json
from datetime import date, datetime

import requests
from dotenv import load_dotenv

from run import (
    BASE_URL,
    api_post,
    column_letter,
    extract_text,
    find_column_index,
    get_sheet_plain_values,
    get_tenant_access_token,
    resolve_spreadsheet_token,
    update_single_cell,
)

load_dotenv()

# Target Base IDs for KL Master view
TARGET_BASE_APP_ID = os.getenv("KL_MASTER_BASE_APP_ID")
TARGET_TABLE_ID = os.getenv("KL_MASTER_TABLE_ID")
TARGET_VIEW_ID = os.getenv("KL_MASTER_VIEW_ID")

# Main Base IDs from env (existing production table/view)
BASE_APP_TOKEN = os.getenv("BASE_APP_TOKEN")
BASE_TABLE_ID = os.getenv("BASE_TABLE_ID")
BASE_VIEW_ID = os.getenv("BASE_VIEW_ID")
REPORT_GROUP_ID = os.getenv("REPORT_GROUP_ID")
TRACKER_WIKI_TOKEN = os.getenv("TRACKER_WIKI_TOKEN")
TRACKER_SHEET_ID = os.getenv("TRACKER_SHEET_ID")


def normalize_text(value):
    return " ".join(str(value or "").strip().lower().split())


def get_task_name(fields):
    return extract_text(fields.get("Task Name", "")) or extract_text(fields.get("Task Name/Doc", ""))


def get_ongoing_appeals(token):
    """Fetch KL Master ongoing records, then keep only overdue tasks (end_date < today)."""
    today = date.today()
    url = f"{BASE_URL}/open-apis/bitable/v1/apps/{TARGET_BASE_APP_ID}/tables/{TARGET_TABLE_ID}/records/search"
    records = []
    page_token = None

    while True:
        payload = {
            "view_id": TARGET_VIEW_ID,
            "page_size": 500,
            "filter": {
                "conjunction": "and",
                "conditions": [
                    {
                        "field_name": "Appeal Status",
                        "operator": "is",
                        "value": ["Ongoing"],
                    }
                ],
            },
        }
        if page_token:
            payload["page_token"] = page_token

        data = api_post(url, token, payload)
        items = data["data"].get("items", [])
        records.extend(items)

        if data["data"].get("has_more"):
            page_token = data["data"]["page_token"]
        else:
            break

    overdue_records = []
    for rec in records:
        end_date_value = rec.get("fields", {}).get("End date (EOD 11:59 PM)", "")
        if not end_date_value:
            continue
        try:
            if isinstance(end_date_value, int):
                end_date = datetime.fromtimestamp(end_date_value / 1000).date()
            elif isinstance(end_date_value, str):
                end_date = date.fromisoformat(end_date_value)
            else:
                continue
            if end_date < today:
                overdue_records.append(rec)
        except (ValueError, TypeError):
            continue

    return overdue_records


def get_main_base_records(token):
    """Fetch records from main Base view configured in env."""
    url = f"{BASE_URL}/open-apis/bitable/v1/apps/{BASE_APP_TOKEN}/tables/{BASE_TABLE_ID}/records/search"
    records = []
    page_token = None

    while True:
        payload = {"view_id": BASE_VIEW_ID, "page_size": 500}
        if page_token:
            payload["page_token"] = page_token

        data = api_post(url, token, payload)
        items = data["data"].get("items", [])
        records.extend(items)

        if data["data"].get("has_more"):
            page_token = data["data"]["page_token"]
        else:
            break

    return records


def find_tasks_eligible_for_completion(overdue_records, main_base_records):
    """Return normalized overdue task names eligible for auto-completion.

    Eligible when:
    - all matching main-base records have Arbitrator Decision filled, or
    - no matching task exists in main-base records.
    """
    overdue_task_names = {
        normalize_text(get_task_name(rec.get("fields", {})))
        for rec in overdue_records
        if normalize_text(get_task_name(rec.get("fields", {})))
    }

    decisions_by_task = {}
    for rec in main_base_records:
        fields = rec.get("fields", {})
        task_name = normalize_text(get_task_name(fields))
        if task_name not in overdue_task_names:
            continue
        decision = extract_text(fields.get("Arbitrator Decision", ""))
        decisions_by_task.setdefault(task_name, []).append(decision)

    eligible_task_names = set()
    unattended_task_names = set()
    for task_name, decisions in decisions_by_task.items():
        if decisions and all(normalize_text(decision) for decision in decisions):
            eligible_task_names.add(task_name)
        elif any(not normalize_text(decision) for decision in decisions):
            unattended_task_names.add(task_name)

    # Auto-complete tasks that are not found in target (main base) records.
    for task_name in overdue_task_names:
        if task_name not in decisions_by_task:
            eligible_task_names.add(task_name)

    return eligible_task_names, unattended_task_names


def send_unattended_overdue_alert(token, overdue_records, unattended_task_names):
    """Notify report group about overdue tasks that still have unattended appeals."""
    if not unattended_task_names:
        return False
    if not REPORT_GROUP_ID:
        print("Warning: REPORT_GROUP_ID not configured; unattended alert not sent.")
        return False

    display_names = []
    seen = set()
    for rec in overdue_records:
        task_name = get_task_name(rec.get("fields", {}))
        normalized = normalize_text(task_name)
        if normalized in unattended_task_names and normalized not in seen:
            display_names.append(task_name or normalized)
            seen.add(normalized)

    if not display_names:
        return False

    task_lines = "\n".join(f"- {name}" for name in display_names)
    today = date.today().isoformat()
    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"Overdue Appeal Alert - {today}"},
            "template": "red",
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": (
                        "**Unattended appeals detected**\n"
                        "The following task(s) are overdue and still have empty Arbitrator Decision:\n\n"
                        f"{task_lines}"
                    ),
                },
            }
        ],
    }

    url = f"{BASE_URL}/open-apis/im/v1/messages"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "receive_id": REPORT_GROUP_ID,
        "msg_type": "interactive",
        "content": json.dumps(card),
    }

    resp = requests.post(url, headers=headers, params={"receive_id_type": "chat_id"}, json=payload)
    if not resp.ok:
        raise RuntimeError(f"Failed to send unattended alert: {resp.status_code} {resp.text}")

    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Failed to send unattended alert: {data}")

    return True


def resolve_release_status_field(overdue_records):
    """Find a likely field in KL Master for the 'Appeal Results To be Released' value."""
    candidates = ["Task Status", "Status", "Appeal Result Status", "Appeal Result"]
    for rec in overdue_records:
        fields = rec.get("fields", {})
        for candidate in candidates:
            if candidate in fields:
                return candidate
    return None


def update_kl_master_for_completed_tasks(token, overdue_records, completed_task_names):
    """Update KL Master rows for eligible tasks.

    - Appeal Status -> Completed
    - release status field (if present) -> Appeal Results To be Released
    """
    if not completed_task_names:
        return 0, None, set()

    release_status_field = resolve_release_status_field(overdue_records)
    updated = 0
    updated_task_names = set()

    for rec in overdue_records:
        fields = rec.get("fields", {})
        task_name = normalize_text(get_task_name(fields))
        if task_name not in completed_task_names:
            continue

        record_id = rec.get("record_id")
        if not record_id:
            continue

        update_fields = {"Appeal Status": "Completed"}
        if release_status_field:
            update_fields[release_status_field] = "Appeal Results To be Released"

        url = f"{BASE_URL}/open-apis/bitable/v1/apps/{TARGET_BASE_APP_ID}/tables/{TARGET_TABLE_ID}/records/{record_id}"
        payload = {"fields": update_fields}
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        }

        resp = requests.put(url, headers=headers, json=payload)
        if not resp.ok:
            raise RuntimeError(f"Failed to update KL Master record {record_id}: {resp.status_code} {resp.text}")

        data = resp.json()
        if data.get("code") != 0:
            raise RuntimeError(f"Failed to update KL Master record {record_id}: {data}")

        updated += 1
        updated_task_names.add(task_name)

    return updated, release_status_field, updated_task_names


def resolve_tracker_spreadsheet_token(token):
    """Resolve tracker wiki token to spreadsheet token, fallback to raw token."""
    if not TRACKER_WIKI_TOKEN:
        raise RuntimeError("TRACKER_WIKI_TOKEN is not configured in .env")

    resource = {"type": "wiki", "token": TRACKER_WIKI_TOKEN, "sheet_id": TRACKER_SHEET_ID}
    try:
        return resolve_spreadsheet_token(token, resource)
    except RuntimeError:
        return TRACKER_WIKI_TOKEN


def update_tracker_status_for_completed_tasks(token, completed_task_names):
    """Set tracker Task Status to 'Accuracy Finalized' for completed tasks."""
    if not completed_task_names:
        return 0
    if not TRACKER_SHEET_ID:
        print("Warning: TRACKER_SHEET_ID not configured; tracker update skipped.")
        return 0

    spreadsheet_token = resolve_tracker_spreadsheet_token(token)
    rows = get_sheet_plain_values(token, spreadsheet_token, TRACKER_SHEET_ID)
    if not rows:
        return 0

    headers = [str(cell).strip() if cell else "" for cell in rows[0]]
    task_col = find_column_index(headers, "Task Name/Doc", "Task Name", "Task")
    status_col = find_column_index(headers, "Task Status", "Status")

    updated = 0
    status_col_letter = column_letter(status_col)
    for row_index, row in enumerate(rows[1:], start=2):
        task_value = ""
        if task_col < len(row):
            task_value = str(row[task_col] or "").strip()
        if normalize_text(task_value) not in completed_task_names:
            continue

        target_range = f"{TRACKER_SHEET_ID}!{status_col_letter}{row_index}:{status_col_letter}{row_index}"
        update_single_cell(token, spreadsheet_token, target_range, "Accuracy Finalized")
        updated += 1

    return updated


def send_finalized_card(token, overdue_records, updated_task_names):
    """Send an interactive card to report group listing tasks finalized in this run."""
    if not updated_task_names or not REPORT_GROUP_ID:
        return False

    display_names = []
    seen = set()
    for rec in overdue_records:
        task_name = get_task_name(rec.get("fields", {}))
        normalized = normalize_text(task_name)
        if normalized in updated_task_names and normalized not in seen:
            display_names.append(task_name or normalized)
            seen.add(normalized)

    if not display_names:
        return False

    today = date.today().isoformat()
    task_lines = "\n".join(f"- {name}" for name in display_names)

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"Appeals Finalized - {today}"},
            "template": "green",
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": (
                        f"**{len(display_names)} task(s) have been finalized**\n\n"
                        "The following tasks have been updated to:\n"
                        "- **Appeal Status** → Completed\n"
                        "- **Tracker Task Status** → Accuracy Finalized\n\n"
                        f"{task_lines}"
                    ),
                },
            }
        ],
    }

    url = f"{BASE_URL}/open-apis/im/v1/messages"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "receive_id": REPORT_GROUP_ID,
        "msg_type": "interactive",
        "content": json.dumps(card),
    }

    resp = requests.post(url, headers=headers, params={"receive_id_type": "chat_id"}, json=payload)
    if not resp.ok:
        raise RuntimeError(f"Failed to send finalized card: {resp.status_code} {resp.text}")

    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Failed to send finalized card: {data}")

    return True


def process_ongoing_appeals(token):
    """Main processing logic for closing overdue tasks with complete arbitration."""
    print("\n=== POST-PROCESSING: Complete Overdue Appeals in KL Master ===")

    overdue_records = get_ongoing_appeals(token)
    if not overdue_records:
        print("No overdue tasks with 'Ongoing' appeal status found.")
        return

    main_base_records = get_main_base_records(token)
    completed_task_names, unattended_task_names = find_tasks_eligible_for_completion(overdue_records, main_base_records)

    if unattended_task_names:
        sent = send_unattended_overdue_alert(token, overdue_records, unattended_task_names)
        if sent:
            print(f"Unattended overdue alert sent for {len(unattended_task_names)} task(s).")

    if not completed_task_names:
        print("No overdue ongoing tasks are eligible for auto-completion.")
        return

    updated_count, release_status_field, updated_task_names = update_kl_master_for_completed_tasks(
        token,
        overdue_records,
        completed_task_names,
    )

    tracker_updated_count = update_tracker_status_for_completed_tasks(token, updated_task_names)

    print(f"\nTask(s) eligible for completion: {len(completed_task_names)}")
    print(f"KL Master row(s) updated: {updated_count}")
    print(f"Tracker row(s) updated to Accuracy Finalized: {tracker_updated_count}")
    if release_status_field:
        print(f"Release-status field updated: {release_status_field}")
    else:
        print("Release-status field not found in KL Master view; only 'Appeal Status' was updated.")

    if updated_task_names:
        sent = send_finalized_card(token, overdue_records, updated_task_names)
        if sent:
            print(f"Finalized summary card sent for {len(updated_task_names)} task(s).")

    print("\nPost-processing complete.")


def main():
    token = get_tenant_access_token()
    process_ongoing_appeals(token)


if __name__ == "__main__":
    main()
