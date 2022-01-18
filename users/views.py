from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializer import UserSerializer
from .permission import UserPermission

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
  permission_classes = (UserPermission, )

  def get_object(self):
    # オブジェクトを取得
    if self.kwargs.get("pk") == "current" and self.request.user:
      obj = self.request.user
    else:
      obj = super(UserViewSet, self).get_object()

    #パーミッションを検証
    self.check_object_permissions(self.request, obj)

    return obj