import requests
from decouple import config
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = "Try to get test user token"

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        self.stdout.write("Start to get test user token")

        token = self._generate_userToken()

        self.stdout.write(str(token))

    def _generate_userToken(self):
        API_KEY = config("FIREBASE_API_KEY")
        TEST_FIREBASE_EMAIL = config("TEST_FIREBASE_EMAIL")
        TEST_FIREBASE_PASSWORD = config("TEST_FIREBASE_PASSWORD")
        uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={API_KEY}"
        data = {
            "email": TEST_FIREBASE_EMAIL,
            "password": TEST_FIREBASE_PASSWORD,
            "returnSecureToken": True,
        }
        result = requests.post(url=uri, data=data).json()
        return result["idToken"]
