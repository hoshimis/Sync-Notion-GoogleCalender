from Notion.get_db_item import get_db_item
from google_calender.add_event import add_event
from google_calender.get_event import get_event
import json


def main():
    # 指定したNotionのDBより、全てのitemを取得する
    result = get_db_item()
    formatted_result = json.dumps(result, indent=2, ensure_ascii=False)

    # Googleのカレンダーにイベントを追加する
    notion_event_lists = []
    # Notion からは すべて終日のイベントとして取得する
    for item in result['results']:
        # 1件ずつイベントを追加する
        try:
            event = {
                'summary': item['properties']['名前']['title'][0]['plain_text'],
                'start': {
                    'dateTime': f"{item['properties']['実施予定日']['date']['start']}T00:00:00+09:00",
                },
                'end': {
                    'dateTime': f"{item['properties']['実施予定日']['date']['start']}T23:59:59+09:00",
                },
            }
        except:
            continue

        notion_event_lists.append(event)

    # Google カレンダーから 既存のイベントを取得する
    google_event_lists = get_event()

    # Notion と Google カレンダーのイベントを比較する
    # 既存のイベントがあれば、追加しない
    for notion_event in notion_event_lists:
        for google_event in google_event_lists:
            if notion_event['summary'] == google_event['summary']:
                notion_event_lists.remove(notion_event)
                break

    # イベントを追加する
    for item in notion_event_lists:
        add_event(item)


if __name__ == '__main__':
    main()
