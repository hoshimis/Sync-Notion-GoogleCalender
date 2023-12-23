
from datetime import datetime, timezone
from . import check_token


def get_event():
    # Tokenのチェック
    service = check_token.check_token()

    now = datetime.now(timezone.utc).isoformat()

    get_calender_list = service.calendarList().list().execute()['items']

    calender_ids = [item['id'] for item in get_calender_list]

    for calender_id in calender_ids:
        events_result = service.events().list(
            calendarId=calender_id, timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

    return events
