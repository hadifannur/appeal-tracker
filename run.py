import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

SPREADSHEET_TOKEN = os.getenv("SPREADSHEET_TOKEN")
SHEET_ID = os.getenv("SHEET_ID")

BASE_APP_TOKEN = os.getenv("BASE_APP_TOKEN")
BASE_TABLE_ID = os.getenv("BASE_TABLE_ID")
BASE_VIEW_ID = os.getenv("BASE_VIEW_ID")

BASE_URL = "https://open.larkoffice.com"


def get_tenant_access_token():
    url = f"{BASE_URL}/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Failed to get token: {data}")
    return data["tenant_access_token"]


def get_sheet_data(token):
    # Read all data from the sheet (up to row 1000)
    range_str = f"{SHEET_ID}!A1:Z1000"
    url = f"{BASE_URL}/open-apis/sheets/v2/spreadsheets/{SPREADSHEET_TOKEN}/values/{range_str}"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Failed to read sheet: {data}")
    return data["data"]["valueRange"]["values"]


def find_released_tasks(rows):
    if not rows:
        print("No data found in sheet.")
        return

    header = [str(cell).strip() if cell else "" for cell in rows[0]]

    # Find column indices (case-insensitive search)
    task_name_col = None
    task_status_col = None
    for i, h in enumerate(header):
        h_lower = h.lower()
        if "task name" in h_lower or "task" == h_lower:
            task_name_col = i
        if "task status" in h_lower:
            task_status_col = i

    if task_name_col is None or task_status_col is None:
        print(f"Could not find required columns. Headers found: {header}")
        return

    released_tasks = []
    for row in rows[1:]:
        if len(row) <= max(task_name_col, task_status_col):
            continue
        status = str(row[task_status_col]).strip() if row[task_status_col] else ""
        if status == "Appeal Has Been Released":
            cell = row[task_name_col]
            if isinstance(cell, list) and cell and isinstance(cell[0], dict):
                task_name = cell[0].get("text", "").strip()
            elif cell:
                task_name = str(cell).strip()
            else:
                task_name = ""
            released_tasks.append(task_name)

    print(f"\nTasks with status 'Appeal Has Been Released' ({len(released_tasks)} found):")
    for name in released_tasks:
        print(f"  - {name}")

    return released_tasks


def get_base_records(token):
    """Fetch all records from the Base table view."""
    url = f"{BASE_URL}/open-apis/bitable/v1/apps/{BASE_APP_TOKEN}/tables/{BASE_TABLE_ID}/records/search"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    records = []
    page_token = None

    while True:
        payload = {"view_id": BASE_VIEW_ID, "page_size": 500}
        if page_token:
            payload["page_token"] = page_token

        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
        if data.get("code") != 0:
            raise RuntimeError(f"Failed to fetch base records: {data}")

        items = data["data"].get("items", [])
        records.extend(items)

        if data["data"].get("has_more"):
            page_token = data["data"]["page_token"]
        else:
            break

    return records


def extract_text(value):
    """Extract plain text from a Base field value."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                parts.append(item.get("text", ""))
            else:
                parts.append(str(item))
        return "".join(parts).strip()
    return str(value).strip()


def map_tasks_to_base(released_tasks, base_records):
    """Match released tasks against Base records and return appeal initiators."""
    # Build lookup: task name -> list of records (multiple appeals per task)
    base_lookup = {}
    for rec in base_records:
        name = extract_text(rec["fields"].get("Task Name", ""))
        base_lookup.setdefault(name, []).append(rec)

    print(f"\n{'Task Name':<55} {'Appeal Initiator':<45} {'Query':<45} {'Arbitrator Decision'}")
    print("-" * 170)

    for task_name in released_tasks:
        if task_name in base_lookup:
            for rec in base_lookup[task_name]:
                initiator_raw = rec["fields"].get("Appeal Initiator")
                if isinstance(initiator_raw, list):
                    initiator = ", ".join(
                        p.get("name") or p.get("en_name", "") for p in initiator_raw
                    )
                else:
                    initiator = extract_text(initiator_raw)
                query = extract_text(rec["fields"].get("Query", ""))
                decision = extract_text(rec["fields"].get("Arbitrator Decision", ""))
                if decision not in ("Edge Case", "Successful Appeal"):
                    continue
                print(f"  {task_name:<53} {initiator or '(empty)':<45} {query or '(empty)':<45} {decision}")


def main():
    token = get_tenant_access_token()
    rows = get_sheet_data(token)
    released_tasks = find_released_tasks(rows)

    if released_tasks:
        base_records = get_base_records(token)
        map_tasks_to_base(released_tasks, base_records)


if __name__ == "__main__":
    main()
