from base64 import decode
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from firebase_admin import auth, exceptions

from .models import FirebaseUser as User
from .serializer import FirebaseUserSerializer as UserSerializer


# 認証クラスBaseAuthenticationを継承することでカスタムできる
class FirebaseAuthentication(BaseAuthentication):
    keyword = "Bearer"
    model = None

    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()  # headerがここ
        # ログインの例外処理
        if not auth_header:
            return None  # 認証なし

        if (
            len(auth_header) != 2
            or auth_header[0].lower() != self.keyword.lower().encode()
        ):  # トークンの構成が不正
            raise auth.InvalidIdTokenError("Invalid auth token")

        id_token = auth_header.pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token, check_revoked=True)
        except auth.RevokedIdTokenError:
            raise exceptions.FirebaseError("Your auth token expired")
        except Exception:
            raise auth.InvalidIdTokenError("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token["uid"]

            # firebaseと同期するデータを取得
            data = {
                "id": uid,
                "screen_name": decoded_token.get(
                    "name", f"名無しの{decoded_token['email'][:3]}"
                ),
                "email": decoded_token["email"],
                "picture": decoded_token.get("picture", ""),
            }
        except Exception as e:
            raise exceptions.FirebaseError("Firebase Sync Error")

        user = None
        try:
            user = User.objects.get(pk=uid)
            serializer = UserSerializer(user, data=data)
        except User.DoesNotExist:
            serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            raise exceptions.FirebaseError("Failed to convert to user object")

        if not user:
            User.objects.get(pk=serializer.data["id"])

        return (user, None)

    def authenticate_header(self, request):
        pass
