"""
Auto-generated test suite for verifying API state changes and task completion.
"""

import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

try:
    import pytest
except ImportError:
    pytest = None

# URL constants
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8010")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8011")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8012")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8013")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8014")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode("utf-8"))


def api_get(base_url, endpoint):
    return _request("GET", f"{base_url}{endpoint}")


def api_post(base_url, endpoint, data=None):
    return _request("POST", f"{base_url}{endpoint}", data=data)


def _get(url):
    return _request("GET", url)


def _post(url, data=None):
    return _request("POST", url, data=data)


def read_file(path):
    with open(path) as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


def _business_endpoint_count(summary):
    endpoints = summary.get("endpoints", {})
    total = 0
    for ep, info in endpoints.items():
        if "/audit" in ep or "/health" in ep:
            continue
        total += info.get("count", 0)
    return total


def _endpoint_called(summary, needle):
    endpoints = summary.get("endpoints", {})
    for ep, info in endpoints.items():
        if needle.lower() in ep.lower() and info.get("count", 0) > 0:
            return True
    return False


def _audit_requests(base_url):
    data = api_get(base_url, "/audit/requests")
    return data.get("requests", [])


# ---------------------------------------------------------------------------
# test_behavioral_* — verify expected endpoints were called
# ---------------------------------------------------------------------------

def test_behavioral_airtable_crew_records_queried():
    """Agent must query Airtable tblCrew records to determine crew eligibility."""
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    called = _endpoint_called(summary, "tblCrew")
    assert called


def test_behavioral_airtable_equipment_record_updated():
    """Agent must issue a write call to update equipment record rec-eq-001 in tblEquipment."""
    requests = _audit_requests(AIRTABLE_API_URL)
    write_calls = sum(
        1 for entry in requests
        if entry.get("method", "").upper() in ("PATCH", "PUT", "POST")
        and "rec-eq-001" in (entry.get("path") or "")
    )
    assert write_calls > 0


def test_behavioral_google_calendar_events_queried():
    """Agent must query Google Calendar events to identify the October 3 2026 time trial."""
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    called = _endpoint_called(summary, "events")
    assert called


def test_behavioral_airtable_races_queried():
    """Agent must query Airtable tblRaces to cross-reference the October 3 2026 race entry."""
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    called = _endpoint_called(summary, "tblRaces")
    assert called


# ---------------------------------------------------------------------------
# test_outcome_* — verify correct state was reached
# ---------------------------------------------------------------------------

def test_outcome_airtable_marcus_reyes_lapsed():
    """Marcus Reyes record rec-cr-002 must show MembershipStatus Lapsed in live Airtable for season 2026."""
    requests = _audit_requests(AIRTABLE_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "rec-cr-002" in body and "Lapsed" in body:
            found += 1
    assert found > 0


def test_outcome_airtable_equipment_total_quote_430():
    """Equipment record rec-eq-001 must show TotalQuote of 430 in the Airtable response."""
    requests = _audit_requests(AIRTABLE_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "rec-eq-001" in body and ("430" in body):
            found += 1
    assert found > 0


def test_outcome_airtable_equipment_status_pending_approval():
    """Equipment record rec-eq-001 InvoiceStatus must be pending-approval in the Airtable response."""
    requests = _audit_requests(AIRTABLE_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "rec-eq-001" in body and "pending-approval" in body:
            found += 1
    assert found > 0


def test_outcome_google_calendar_time_trial_start_time():
    """Calendar event evt-001 must have a start time of 06:00 HST retrieved during the session."""
    requests = _audit_requests(GOOGLE_CALENDAR_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "evt-001" in body and "06:00" in body:
            found += 1
    assert found > 0


def test_outcome_google_calendar_practice_event_retrieved():
    """Calendar event evt-006 practice session at 05:00 must have been retrieved during the session."""
    requests = _audit_requests(GOOGLE_CALENDAR_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "evt-006" in body and "05:00" in body:
            found += 1
    assert found > 0


def test_outcome_airtable_marcus_reyes_season_2026():
    """Marcus Reyes record for season 2026 must have been retrieved from Airtable."""
    requests = _audit_requests(AIRTABLE_API_URL)
    found = 0
    for entry in requests:
        body = entry.get("response_body") or ""
        if "Marcus Reyes" in body and "2026" in body:
            found += 1
    assert found > 0


# ---------------------------------------------------------------------------
# test_negative_weight_* — detect forbidden behavior (positive assertion + negative weight)
# ---------------------------------------------------------------------------

def test_negative_weight_notion_distractor():
    """Negative test: passes when the forbidden behavior is detected; its negative weight contributes as a penalty."""
    summary = api_get(NOTION_API_URL, "/audit/summary")
    business = _business_endpoint_count(summary)
    assert business > 0


def test_negative_weight_strava_distractor():
    """Negative test: passes when the forbidden behavior is detected; its negative weight contributes as a penalty."""
    summary = api_get(STRAVA_API_URL, "/audit/summary")
    business = _business_endpoint_count(summary)
    assert business > 0


def test_negative_weight_myfitnesspal_distractor():
    """Negative test: passes when the forbidden behavior is detected; its negative weight contributes as a penalty."""
    summary = api_get(MYFITNESSPAL_API_URL, "/audit/summary")
    business = _business_endpoint_count(summary)
    assert business > 0


def test_negative_weight_airtable_equipment_autopaid():
    """Negative test: passes when the forbidden behavior is detected; its negative weight contributes as a penalty."""
    requests = _audit_requests(AIRTABLE_API_URL)
    autopaid = 0
    for entry in requests:
        method = (entry.get("method") or "").upper()
        path = entry.get("path") or ""
        body = (entry.get("request_body") or "").lower()
        if method in ("PATCH", "PUT", "POST") and "rec-eq-001" in path and "paid" in body:
            autopaid += 1
    assert autopaid > 0
