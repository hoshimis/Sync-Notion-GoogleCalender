from . import check_token


def add_event(event):
    # service の取得
    service = check_token.check_token()
    created_event = service.events().insert(
        calendarId="primary", body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
