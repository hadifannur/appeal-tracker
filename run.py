import os
from urllib.parse import parse_qs, urlparse

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
REPORT_GROUP_ID = os.getenv("REPORT_GROUP_ID")

BASE_URL = "https://open.larkoffice.com"
DECISIONS_TO_UPDATE = {"Edge Case", "Successful Appeal", "Both Wrong"}
PERF_TRACKER_SHEET_ID = "FVqt9p"


def get_tenant_access_token():
    url = f"{BASE_URL}/open-apis/auth/v3/tenant_access_token/internal"
    payload = {"app_id": APP_ID, "app_secret": APP_SECRET}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"Failed to get token: {data}")
    return data["tenant_access_token"]


def api_get(url, token, params=None):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"GET failed: {url} -> {data}")
    return data


def api_post(url, token, payload):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json=payload)
    if not resp.ok:
        raise RuntimeError(f"POST {resp.status_code} for {url} | body: {resp.text} | payload: {payload}")
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"POST failed: {url} -> {data}")
    return data


def api_put(url, token, payload):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    resp = requests.put(url, headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"PUT failed: {url} -> {data}")
    return data


def normalize_text(value):
    return " ".join(str(value or "").strip().lower().split())


def find_column_index(headers, *candidates):
    normalized_headers = [normalize_text(header) for header in headers]
    for candidate in candidates:
        normalized_candidate = normalize_text(candidate)
        if normalized_candidate in normalized_headers:
            return normalized_headers.index(normalized_candidate)
    raise RuntimeError(f"Could not find required column. Headers found: {headers}")


def column_letter(index):
    result = ""
    current = index + 1
    while current > 0:
        current, remainder = divmod(current - 1, 26)
        result = chr(65 + remainder) + result
    return result


def parse_sheet_resource(url):
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    query = parse_qs(parsed.query)
    sheet_id = (query.get("sheet") or [None])[0]

    if len(parts) >= 2 and parts[0] == "wiki":
        return {"type": "wiki", "token": parts[1], "sheet_id": sheet_id}
    if len(parts) >= 2 and parts[0] == "sheets":
        return {"type": "sheet", "token": parts[1], "sheet_id": sheet_id}

    raise RuntimeError(f"Unsupported sheet URL: {url}")


def resolve_spreadsheet_token(token, resource):
    if resource["type"] == "sheet":
        return resource["token"]

    url = f"{BASE_URL}/open-apis/wiki/v2/spaces/get_node"
    data = api_get(url, token, params={"token": resource["token"]})
    return data["data"]["node"]["obj_token"]


def get_tracker_spreadsheet_token(token):
    resource = {"type": "wiki", "token": SPREADSHEET_TOKEN, "sheet_id": SHEET_ID}
    try:
        return resolve_spreadsheet_token(token, resource)
    except RuntimeError:
        return SPREADSHEET_TOKEN


def get_sheet_metadata(token, spreadsheet_token):
    url = f"{BASE_URL}/open-apis/sheets/v2/spreadsheets/{spreadsheet_token}/metainfo"
    data = api_get(url, token)
    return data["data"]


def get_sheet_properties(token, spreadsheet_token, sheet_id):
    url = f"{BASE_URL}/open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}"
    data = api_get(url, token)
    return data["data"]["sheet"]


def col_num_to_letter(n):
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result


def resolve_sheet_target(token, url):
    resource = parse_sheet_resource(url)
    spreadsheet_token = resolve_spreadsheet_token(token, resource)
    sheet_id = resource["sheet_id"]

    if not sheet_id:
        sheet_id = get_task_data_record_id(token, spreadsheet_token)

    return spreadsheet_token, sheet_id


def get_sheet_plain_values(token, spreadsheet_token, sheet_id, range_str=None):
    url = f"{BASE_URL}/open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/values/batch_get_plain"
    if not range_str:
        props = get_sheet_properties(token, spreadsheet_token, sheet_id)
        grid = props.get("grid_properties", {})
        col_count = grid.get("column_count", 26)
        row_count = grid.get("row_count", 1000)
        range_str = f"{sheet_id}!A1:{col_num_to_letter(col_count)}{row_count}"
    payload = {"ranges": [range_str]}
    data = api_post(url, token, payload)
    value_ranges = data["data"].get("value_ranges", [])
    if not value_ranges:
        return []
    return value_ranges[0].get("values", [])


def get_sheet_rich_values(token, spreadsheet_token, sheet_id, range_str):
    url = f"{BASE_URL}/open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}/values/batch_get"
    payload = {"ranges": [range_str]}
    data = api_post(url, token, payload)
    value_ranges = data["data"].get("value_ranges", [])
    if not value_ranges:
        return []
    return value_ranges[0].get("values", [])


def update_single_cell(token, spreadsheet_token, range_str, value):
    url = f"{BASE_URL}/open-apis/sheets/v2/spreadsheets/{spreadsheet_token}/values"
    payload = {"valueRange": {"range": range_str, "values": [[value]]}}
    api_put(url, token, payload)


def get_cell(row, index):
    if index >= len(row):
        return ""
    return row[index]


def get_plain_cell_text(row, index):
    value = get_cell(row, index)
    if value is None:
        return ""
    return str(value).strip()


def extract_rich_text(cell):
    parts = []
    for element in cell or []:
        element_type = element.get("type")
        if element_type == "text":
            parts.append(element.get("text", {}).get("text", ""))
        elif element_type == "link":
            parts.append(element.get("link", {}).get("text", ""))
        elif element_type == "mention_document":
            parts.append(element.get("mention_document", {}).get("title", ""))
        elif element_type == "mention_user":
            parts.append(element.get("mention_user", {}).get("name", ""))
        elif element_type == "value":
            parts.append(str(element.get("value", {}).get("value", "")))
    return "".join(parts).strip()


def extract_link_url(cell):
    for element in cell or []:
        element_type = element.get("type")
        if element_type == "link":
            link = element.get("link", {}).get("link")
            if link:
                return link
        if element_type == "mention_document":
            document = element.get("mention_document", {})
            if document.get("object_type") == "sheet" and document.get("token"):
                return f"https://bytedance.larkoffice.com/sheets/{document['token']}"
    return None


def get_sheet_data(token):
    spreadsheet_token = get_tracker_spreadsheet_token(token)
    return get_sheet_plain_values(token, spreadsheet_token, SHEET_ID)


def find_released_tasks(rows):
    if not rows:
        print("No data found in sheet.")
        return []

    header = [str(cell).strip() if cell else "" for cell in rows[0]]

    task_name_col = find_column_index(header, "Task Name/Doc", "Task Name", "Task")
    task_status_col = find_column_index(header, "Task Status", "Status")

    released_tasks = []
    for row in rows[1:]:
        if len(row) <= max(task_name_col, task_status_col):
            continue
        status = str(row[task_status_col]).strip() if row[task_status_col] else ""
        if status in ("Appeal Has Been Released", "Pending Completion from QA"):
            cell = row[task_name_col]
            if isinstance(cell, list) and cell and isinstance(cell[0], dict):
                task_name = cell[0].get("text", "").strip()
            elif cell:
                task_name = str(cell).strip()
            else:
                task_name = ""
            released_tasks.append(task_name)

    print(f"\nTasks with status 'Appeal Has Been Released' or 'Pending Completion from QA' ({len(released_tasks)} found):")
    for name in released_tasks:
        print(f"  - {name}")

    return released_tasks


def get_base_records(token):
    """Fetch all records from the Base table view."""
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


def extract_person_emails(value):
    if not isinstance(value, list):
        text = extract_text(value)
        return [text] if text else []

    emails = []
    for person in value:
        if not isinstance(person, dict):
            continue
        email = (person.get("email") or "").strip()
        if email:
            emails.append(email)
    return emails


def map_tasks_to_base(released_tasks, base_records):
    """Match released tasks against Base records and return actionable appeal items."""
    # Build lookup: task name -> list of records (multiple appeals per task)
    base_lookup = {}
    for rec in base_records:
        name = extract_text(rec["fields"].get("Task Name", ""))
        base_lookup.setdefault(name, []).append(rec)

    print(f"\n{'Task Name':<55} {'Appeal Initiator Email':<45} {'Query':<45} {'Arbitrator Decision'}")
    print("-" * 170)

    appeal_items = []

    for task_name in released_tasks:
        if task_name in base_lookup:
            for rec in base_lookup[task_name]:
                initiator_raw = rec["fields"].get("Appeal Initiator")
                initiator_emails = extract_person_emails(initiator_raw)
                initiator = ", ".join(initiator_emails) if initiator_emails else extract_text(initiator_raw)
                query = extract_text(rec["fields"].get("Query", ""))
                poc_decision = extract_text(rec["fields"].get("POC Decision", ""))
                arbitrator_decision = extract_text(rec["fields"].get("Arbitrator Decision", ""))
                eval_round_dispute = extract_text(rec["fields"].get("Evaluation Round Dispute", ""))
                force_sp_qa_one = (
                    normalize_text(arbitrator_decision) == "successful appeal"
                    and normalize_text(eval_round_dispute) == "poc round"
                )
                if poc_decision in DECISIONS_TO_UPDATE:
                    decision = poc_decision
                elif poc_decision == "Failed Appeal" and arbitrator_decision in DECISIONS_TO_UPDATE:
                    decision = "POC Failed"
                elif not poc_decision and arbitrator_decision in DECISIONS_TO_UPDATE:
                    decision = arbitrator_decision
                else:
                    continue
                qa_raw = rec["fields"].get("Quality Analyst")
                qa_emails = extract_person_emails(qa_raw) if qa_raw else []
                print(f"  {task_name:<53} {initiator or '(empty)':<45} {query or '(empty)':<45} {decision}")

                appeal_items.append(
                    {
                        "task_name": task_name,
                        "query": query,
                        "initiator_emails": initiator_emails,
                        "qa_emails": qa_emails,
                        "decision": decision,
                        "force_sp_qa_one": force_sp_qa_one,
                    }
                )

    return appeal_items


def build_tracker_link_lookup(token, rows):
    spreadsheet_token = get_tracker_spreadsheet_token(token)
    headers = [str(cell).strip() if cell else "" for cell in rows[0]]
    extracted_col = find_column_index(headers, "Extracted/Appeal Doc", "Extracted/Appeal")
    column = column_letter(extracted_col)
    rich_range = f"{SHEET_ID}!{column}1:{column}{len(rows)}"
    rich_values = get_sheet_rich_values(token, spreadsheet_token, SHEET_ID, rich_range)

    link_lookup = {}
    for row_index in range(1, len(rows)):
        task_name = get_plain_cell_text(rows[row_index], extracted_col)
        if not task_name:
            continue
        rich_cell = []
        if row_index < len(rich_values) and rich_values[row_index]:
            rich_cell = rich_values[row_index][0]
        link_url = extract_link_url(rich_cell)
        if not link_url and rich_cell:
            link_text = extract_rich_text(rich_cell)
            if link_text.startswith("http://") or link_text.startswith("https://"):
                link_url = link_text

        link_lookup.setdefault(task_name, []).append({"url": link_url})

    return link_lookup


def row_matches_query_and_email(row, query_col, user_col, query, emails):
    row_query = normalize_text(get_plain_cell_text(row, query_col))
    if row_query != normalize_text(query):
        return False

    user_value = normalize_text(get_plain_cell_text(row, user_col))
    return any(normalize_text(email) and normalize_text(email) in user_value for email in emails)


def read_sp_before_from_link(token, link_url, query, initiator_emails):
    """Read SP's Accuracy Before Appeal (column R, index 17) from the linked task data sheet."""
    if not link_url:
        return None

    spreadsheet_token, sheet_id = resolve_sheet_target(token, link_url)
    rows = get_sheet_plain_values(token, spreadsheet_token, sheet_id)
    if not rows:
        return None

    headers = [str(cell).strip() if cell else "" for cell in rows[0]]
    query_col = find_column_index(headers, "Query")
    user_col = find_column_index(headers, "User")
    try:
        before_col = find_column_index(headers, "Accuracy before appeal", "SP Accuracy Before Appeal", "Accuracy Before Appeal")
    except RuntimeError:
        before_col = 17  # Fallback to column R

    for row in rows[1:]:
        if row_matches_query_and_email(row, query_col, user_col, query, initiator_emails):
            return get_plain_cell_text(row, before_col) or None

    return None


def update_accuracy_for_link(token, link_url, query, initiator_emails, value=1):
    """Update Accuracy after appeal in the linked sheet. Returns (success, message, spreadsheet_token)."""
    if not link_url:
        return False, "missing link", None

    spreadsheet_token, sheet_id = resolve_sheet_target(token, link_url)
    rows = get_sheet_plain_values(token, spreadsheet_token, sheet_id)
    if not rows:
        return False, "linked sheet is empty", spreadsheet_token

    headers = [str(cell).strip() if cell else "" for cell in rows[0]]
    query_col = find_column_index(headers, "Query")
    user_col = find_column_index(headers, "User")
    accuracy_col = find_column_index(headers, "Accuracy after appeal", "SP Accuracy After Appeal", "QA Accuracy After Appeal", "Accuracy After Appeal")

    for row_index, row in enumerate(rows[1:], start=2):
        if row_matches_query_and_email(row, query_col, user_col, query, initiator_emails):
            accuracy_range = f"{sheet_id}!{column_letter(accuracy_col)}{row_index}:{column_letter(accuracy_col)}{row_index}"
            update_single_cell(token, spreadsheet_token, accuracy_range, value)
            return True, f"updated {accuracy_range}", spreadsheet_token

    return False, "no matching row found in linked sheet", spreadsheet_token


def get_sheet1_id(token, spreadsheet_token):
    """Return the sheetId of the tab named 'Sheet1', falling back to the first sheet."""
    metadata = get_sheet_metadata(token, spreadsheet_token)
    sheets = metadata.get("sheets", [])
    for sheet in sheets:
        if sheet.get("title", "").strip().lower() == "sheet1":
            return sheet["sheetId"]
    # Fallback: first sheet by index
    sheets_sorted = sorted(sheets, key=lambda s: s.get("index", 0))
    if not sheets_sorted:
        raise RuntimeError(f"No sheets found in spreadsheet: {spreadsheet_token}")
    return sheets_sorted[0]["sheetId"]


def get_task_data_record_id(token, spreadsheet_token):
    """Return the sheetId of the tab named 'Task Data Record', falling back to the first sheet."""
    metadata = get_sheet_metadata(token, spreadsheet_token)
    sheets = metadata.get("sheets", [])
    for sheet in sheets:
        if sheet.get("title", "").strip().lower() == "task data record":
            return sheet["sheetId"]
    # Fallback: first sheet by index
    sheets_sorted = sorted(sheets, key=lambda s: s.get("index", 0))
    if not sheets_sorted:
        raise RuntimeError(f"No sheets found in spreadsheet: {spreadsheet_token}")
    return sheets_sorted[0]["sheetId"]


def read_accuracy_from_sheet1(token, spreadsheet_token, emails, query=None):
    """Read Sheet1 of the linked spreadsheet, find the row matching email (and optionally query),
    and return (user, before_appeal_value, after_appeal_value)."""
    sheet_id = get_sheet1_id(token, spreadsheet_token)
    rows = get_sheet_plain_values(token, spreadsheet_token, sheet_id)
    if not rows:
        return None, None, None

    # Scan all rows for a header row (Sheet1 may have multiple sections)
    user_col = None
    query_col = None
    after_appeal_col = None
    before_appeal_col = None
    header_row_index = None

    for i, row in enumerate(rows):
        headers = [str(cell).strip() if cell else "" for cell in row]
        headers_lower = [h.lower() for h in headers]
        if any("after appeal" in h for h in headers_lower):
            header_row_index = i
            for idx, h in enumerate(headers_lower):
                if "after appeal" in h:
                    after_appeal_col = idx
                if "before appeal" in h:
                    before_appeal_col = idx
                if h == "user":
                    user_col = idx
                if h == "query":
                    query_col = idx
            break

    if after_appeal_col is None:
        return None, None, None

    # Email col fallback: col B (index 1) if no "User" header found
    if user_col is None:
        user_col = 1

    norm_emails = [normalize_text(e) for e in emails if e]
    start = (header_row_index + 1) if header_row_index is not None else 0

    for row in rows[start:]:
        user_value = normalize_text(get_plain_cell_text(row, user_col))
        if not user_value:
            continue
        if not any(e and e in user_value for e in norm_emails):
            continue
        if query and query_col is not None:
            row_query = normalize_text(get_plain_cell_text(row, query_col))
            if row_query != normalize_text(query):
                continue
        display_name = get_plain_cell_text(row, user_col)
        before_value = get_plain_cell_text(row, before_appeal_col) if before_appeal_col is not None else None
        accuracy_value = get_plain_cell_text(row, after_appeal_col)
        return display_name, before_value, accuracy_value

    return None, None, None


def update_perf_tracker_row(token, perf_spt, task_name, email, accuracy_value):
    """Find the row in the individual perf tracker matching email (col G) + task name (col C),
    write accuracy_value to Accuracy After Appeal (col N)."""
    rows = get_sheet_plain_values(token, perf_spt, PERF_TRACKER_SHEET_ID)
    if not rows:
        print(f"    Perf tracker sheet is empty, skipping.")
        return False

    headers = [str(cell).strip() if cell else "" for cell in rows[0]]
    try:
        name_col = find_column_index(headers, "Name")
        task_col = find_column_index(headers, "Task Name")
        accuracy_col = find_column_index(headers, "Accuracy After Appeal")
    except RuntimeError as e:
        print(f"    Could not find columns in perf tracker: {e}")
        return False

    norm_email = normalize_text(email)
    norm_task = normalize_text(task_name)

    for row_index, row in enumerate(rows[1:], start=2):
        row_name = normalize_text(get_plain_cell_text(row, name_col))
        row_task = normalize_text(get_plain_cell_text(row, task_col))
        if norm_email and norm_email in row_name and norm_task == row_task:
            acc_range = f"{PERF_TRACKER_SHEET_ID}!{column_letter(accuracy_col)}{row_index}:{column_letter(accuracy_col)}{row_index}"
            update_single_cell(token, perf_spt, acc_range, accuracy_value)
            print(f"    Perf tracker updated: {email} / {task_name} -> {accuracy_value} ({acc_range})")
            return True

    print(f"    No matching row in perf tracker for: {email} / {task_name}")
    return False


def sync_perf_tracker(token, appeal_items, link_lookup):
    """For each appeal item, read Sheet1 of its linked spreadsheet and push
    Accuracy after appeal to the individual performance tracker."""
    perf_spt = get_tracker_spreadsheet_token(token)

    print("\nSyncing individual performance tracker from linked Sheet1:")
    synced = 0
    sync_results = []  # list of {task_name, email, accuracy_value}

    for item in appeal_items:
        links = link_lookup.get(item["task_name"], [])
        for link_info in links:
            if not link_info.get("spreadsheet_token"):
                continue
            spt = link_info["spreadsheet_token"]

            # SP: normally skip perf tracker update for Both Wrong, unless forced override applies
            if item.get("force_sp_qa_one") or item["decision"] != "Both Wrong":
                display_name, before_value, accuracy_value = read_accuracy_from_sheet1(token, spt, item["initiator_emails"], item["query"])
                if display_name is None:
                    print(f"  - {item['task_name']}: could not find email/accuracy in Sheet1")
                    continue
                raw_accuracy = accuracy_value
                # Convert "93.69%" -> 0.9369
                if isinstance(accuracy_value, str) and accuracy_value.endswith("%"):
                    try:
                        accuracy_value = round(float(accuracy_value.rstrip("%")) / 100, 6)
                    except ValueError:
                        pass
                print(f"  - {item['task_name']} / {display_name}: before={before_value} after={raw_accuracy}")
                if update_perf_tracker_row(token, perf_spt, item["task_name"], display_name, accuracy_value):
                    synced += 1
                sync_results.append({
                    "task_name": item["task_name"],
                    "email": display_name,
                    "decision": item["decision"],
                    "before": before_value,
                    "accuracy": raw_accuracy,
                })

            # QA 3-step flow (same as SP)
            if item.get("qa_emails"):
                # Determine value to write into QA's accuracy after appeal cell
                if item.get("force_sp_qa_one"):
                    qa_write_value = 1
                elif item["decision"] == "Edge Case":
                    qa_write_value = 1
                elif item["decision"] in ("Successful Appeal", "Both Wrong"):
                    # Read SP's before appeal from column R of linked task data sheet
                    sp_before_raw = read_sp_before_from_link(token, link_info["url"], item["query"], item["initiator_emails"])
                    if not sp_before_raw:
                        print(f"  - QA: could not read SP before appeal for {item['task_name']}")
                        break
                    qa_write_value = sp_before_raw
                    if isinstance(qa_write_value, str) and qa_write_value.endswith("%"):
                        try:
                            qa_write_value = round(float(qa_write_value.rstrip("%")) / 100, 6)
                        except ValueError:
                            pass
                elif item["decision"] == "POC Failed":
                    # QA's after-appeal = QA's own before-appeal
                    qa_before_raw = read_sp_before_from_link(token, link_info["url"], item["query"], item["qa_emails"])
                    if not qa_before_raw:
                        print(f"  - QA: could not read QA before appeal for {item['task_name']}")
                        break
                    qa_write_value = qa_before_raw
                    if isinstance(qa_write_value, str) and qa_write_value.endswith("%"):
                        try:
                            qa_write_value = round(float(qa_write_value.rstrip("%")) / 100, 6)
                        except ValueError:
                            pass
                else:
                    break

                # Step 1: write value into QA's accuracy after appeal in linked task data sheet
                update_accuracy_for_link(token, link_info["url"], item["query"], item["qa_emails"], value=qa_write_value)

                # Step 2: read Sheet1 with QA emails
                qa_display, qa_before, qa_accuracy = read_accuracy_from_sheet1(token, spt, item["qa_emails"], item["query"])
                if qa_display is None:
                    print(f"  - QA: could not find QA in Sheet1 for {item['task_name']}")
                    break

                raw_qa_accuracy = qa_accuracy
                if isinstance(qa_accuracy, str) and qa_accuracy.endswith("%"):
                    try:
                        qa_accuracy = round(float(qa_accuracy.rstrip("%")) / 100, 6)
                    except ValueError:
                        pass

                # Step 3: write to individual perf tracker
                print(f"  - QA ({item['decision']}): {qa_display} / {item['task_name']} -> {raw_qa_accuracy}")
                if update_perf_tracker_row(token, perf_spt, item["task_name"], qa_display, qa_accuracy):
                    synced += 1
                sync_results.append({
                    "task_name": item["task_name"],
                    "email": qa_display,
                    "decision": f"{item['decision']} (QA)",
                    "before": qa_before or "-",
                    "accuracy": raw_qa_accuracy,
                })
            break

    print(f"\nPerformance tracker synced for {synced} item(s).")
    return synced, sync_results


def update_accuracy_after_appeal(token, rows, appeal_items):
    link_lookup = build_tracker_link_lookup(token, rows)

    print("\nUpdating linked spreadsheets:")
    updated_count = 0

    for item in appeal_items:
        links = link_lookup.get(item["task_name"], [])
        if not links:
            print(f"  - {item['task_name']}: no matching row found in tracker sheet")
            continue

        item_updated = False
        for link_info in links:
            if item.get("force_sp_qa_one"):
                success, message, spt = update_accuracy_for_link(
                    token,
                    link_info["url"],
                    item["query"],
                    item["initiator_emails"],
                    value=1,
                )
                link_info["spreadsheet_token"] = spt
                if success:
                    print(f"  - {item['task_name']}: forced override applied — SP after-appeal set to 1")
                    updated_count += 1
                    item_updated = True
                break
            if item["decision"] == "Both Wrong":
                # SP stays the same — just resolve the spreadsheet token for Sheet1 sync
                if link_info.get("url"):
                    try:
                        spt, _ = resolve_sheet_target(token, link_info["url"])
                        link_info["spreadsheet_token"] = spt
                        item_updated = True
                        print(f"  - {item['task_name']}: Both Wrong — SP not updated")
                    except Exception as e:
                        print(f"  - {item['task_name']}: could not resolve sheet token: {e}")
                break
            if item["decision"] == "POC Failed":
                # SP's after-appeal = SP's own before-appeal (no change in accuracy)
                if link_info.get("url"):
                    sp_before = read_sp_before_from_link(token, link_info["url"], item["query"], item["initiator_emails"])
                    if sp_before:
                        if isinstance(sp_before, str) and sp_before.endswith("%"):
                            try:
                                sp_before = round(float(sp_before.rstrip("%")) / 100, 6)
                            except ValueError:
                                pass
                        success, message, spt = update_accuracy_for_link(token, link_info["url"], item["query"], item["initiator_emails"], value=sp_before)
                        link_info["spreadsheet_token"] = spt
                        if success:
                            print(f"  - {item['task_name']}: POC Failed — SP after-appeal reset to before-appeal")
                            updated_count += 1
                            item_updated = True
                    else:
                        print(f"  - {item['task_name']}: POC Failed — could not read SP before-appeal")
                break
            success, message, spt = update_accuracy_for_link(
                token,
                link_info["url"],
                item["query"],
                item["initiator_emails"],
            )
            # Store the resolved spreadsheet token for later Sheet1 sync
            link_info["spreadsheet_token"] = spt
            if success:
                print(f"  - {item['task_name']}: {message}")
                updated_count += 1
                item_updated = True
                break

        if not item_updated:
            print(f"  - {item['task_name']}: no linked row matched query + email")

    print(f"\nAccuracy after appeal updated for {updated_count} item(s).")
    return link_lookup



def send_summary_card(token, appeal_items, linked_updated, perf_synced, sync_results):
    """Send an interactive summary card to the report group chat."""
    import json
    from datetime import date

    today = date.today().strftime("%Y-%m-%d")

    # Build rows from sync_results (has accuracy)
    rows_elements = []
    for r in sync_results:
        rows_elements.append({
            "tag": "column_set",
            "flex_mode": "none",
            "background_style": "default",
            "columns": [
                {"tag": "column", "width": "weighted", "weight": 3, "elements": [
                    {"tag": "markdown", "content": r["task_name"]}
                ]},
                {"tag": "column", "width": "weighted", "weight": 2, "elements": [
                    {"tag": "markdown", "content": r["email"]}
                ]},
                {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                    {"tag": "markdown", "content": r["decision"]}
                ]},
                {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                    {"tag": "markdown", "content": str(r["before"]) if r.get("before") else "-"}
                ]},
                {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                    {"tag": "markdown", "content": str(r["accuracy"]) if r["accuracy"] else "-"}
                ]},
            ]
        })

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"Appeal Automation Report — {today}"},
            "template": "blue"
        },
        "elements": [
            {
                "tag": "div",
                "text": {"tag": "lark_md", "content": f"**Released tasks processed:** {len(appeal_items)}\n**Linked sheets updated:** {linked_updated}\n**Performance tracker rows synced:** {perf_synced}"}
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "text": {"tag": "lark_md", "content": "**Accuracy After Appeal per person:**"}
            },
            # Header row
            {
                "tag": "column_set",
                "flex_mode": "none",
                "background_style": "grey",
                "columns": [
                    {"tag": "column", "width": "weighted", "weight": 3, "elements": [
                        {"tag": "markdown", "content": "**Task Name**"}
                    ]},
                    {"tag": "column", "width": "weighted", "weight": 2, "elements": [
                        {"tag": "markdown", "content": "**Email**"}
                    ]},
                    {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                        {"tag": "markdown", "content": "**Decision**"}
                    ]},
                    {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                        {"tag": "markdown", "content": "**Before Appeal**"}
                    ]},
                    {"tag": "column", "width": "weighted", "weight": 1, "elements": [
                        {"tag": "markdown", "content": "**After Appeal**"}
                    ]},
                ]
            },
            *rows_elements,
        ]
    }

    url = f"{BASE_URL}/open-apis/im/v1/messages"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "receive_id": REPORT_GROUP_ID,
        "msg_type": "interactive",
        "content": json.dumps(card),
    }
    resp = requests.post(url, headers=headers, params={"receive_id_type": "chat_id"}, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        print(f"  Warning: Failed to send card: {data}")
    else:
        print("  Summary card sent to group.")


def main():
    token = get_tenant_access_token()
    rows = get_sheet_data(token)
    released_tasks = find_released_tasks(rows)

    if released_tasks:
        base_records = get_base_records(token)
        appeal_items = map_tasks_to_base(released_tasks, base_records)
        if appeal_items:
            link_lookup = update_accuracy_after_appeal(token, rows, appeal_items)
            linked_updated = sum(1 for item in appeal_items for l in link_lookup.get(item["task_name"], []) if l.get("spreadsheet_token"))
            synced_count, sync_results = sync_perf_tracker(token, appeal_items, link_lookup)
            print("\nSending summary card...")
            send_summary_card(token, appeal_items, linked_updated, synced_count, sync_results)


if __name__ == "__main__":
    main()
