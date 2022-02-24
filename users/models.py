from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


class FirebaseUser(models.Model):
    id = models.CharField(
        primary_key=True, max_length=300
    )  # firebase のuidをUserモデルの主キーにする
    screen_name = models.CharField(max_length=64, null=False, blank=False)  # 表示名
    email = models.EmailField(null=False, blank=False)
    picture = models.CharField(
        max_length=300, blank=True, default=""
    )  # ユーザー画像, firebase上に存在
    is_stuff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
