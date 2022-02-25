from rest_framework import viewsets
from rest_framework.response import Response

from .models import FirebaseUser as User
from .serializer import (
    FirebaseUserViewSerializer as UserSerializer,
    FirebaseUserSelfSerializer,
)
from .permission import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get_object(self):
        # オブジェクトを取得
        if self.kwargs.get("pk") == "current" and self.request.user:
            obj = self.request.user
        else:
            return super(UserViewSet, self).get_object()

        # パーミッションを検証
        self.check_object_permissions(self.request, obj)

        return obj

    def get_serializer(self, *args, **kwargs):
        if self.kwargs.get("pk") == "current" and self.request.user:
            serializer_class = FirebaseUserSelfSerializer
            return serializer_class(*args, **kwargs)
        else:
            return super(UserViewSet, self).get_serializer(*args, **kwargs)
