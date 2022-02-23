import time, uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from users.models import FirebaseUser as User


# Create your models here.
class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default="new routine")
    description = models.CharField(
        max_length=200, default="you can write some description"
    )
    start_time = models.TimeField(default=time.time)
    finish_time = models.TimeField(default=time.time)
    owner = models.ForeignKey(
        User, related_name="user_%(class)s", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} object ({self.id}, {self.name}, {self.start_time}, {self.finish_time}, {self.owner})"


class RoutineEveryDay(Routine):
    pass


class RoutineEveryWeek(Routine):
    WEEK_SET = (
        (0, "日"),
        (1, "月"),
        (2, "火"),
        (3, "水"),
        (4, "木"),
        (5, "金"),
        (6, "土"),
    )

    week = models.IntegerField(choices=WEEK_SET, default=0)

    def __str__(self):
        return f"{self.__class__.__name__} object ({self.id}, {self.name}, {self.__class__.WEEK_SET[self.week]}, {self.start_time}, {self.finish_time}, {self.owner})"


class RoutineSpecDay(Routine):
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.__class__.__name__} object ({self.id}, {self.name}, {self.date}, {self.start_time}, {self.finish_time}, {self.owner})"


class Setting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=8, default="F0F0F0FF")
    owner = models.ForeignKey(
        User, related_name="user_routine_setting", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.__class__.__name__} object - {self.owner}'s setting ({self.id}, {self.color})"
