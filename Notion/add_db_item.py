import requests
import os
from dotenv import load_dotenv
load_dotenv()


def add_db_item(item):
    NOTION_API_SECRET = os.getenv('NOTION_API_SECRET')
    NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"

    headers = {
        "Authorization": f"Bearer {NOTION_API_SECRET}",
        "Accept": "application/json",
        "Notion-Version": "2022-06-28"
    }

    pass
