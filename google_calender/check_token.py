import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path


def check_token():
    # スクリプトと同じディレクトリにトークンが保存されているか確認し、なければ作成する
    token_file = os.path.dirname(__file__) + "/" + 'token.json'
    creds = None

    # カレンダーAPIのスコープを設定
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # token_fileが存在するか確認
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file)

    # credsが存在しない、もしくは有効期限が切れている場合は、認証情報を更新する
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # ダウンロードしたクライアントIDのJSONファイル
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.dirname(__file__) + '/' + 'credentials.json',
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        # 作成した認証情報を 'token.json' ファイルに保存
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = googleapiclient.discovery.build(
        'calendar', 'v3', credentials=creds)

    return service
