from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    owner = models.ForeignKey(
        "users.User", related_name="routine", on_delete=models.CASCADE
    )


class RoutineEveryDay(Routine):
    pass


class RoutineEveryWeek(Routine):
    week = models.IntegerField()


class RoutineSpecDay(Routine):
    date = models.DateField()


class Setting(models.Model):
    color = models.CharField(max_length=8)
    owner = models.ForeignKey(
        "users.User", related_name="routine_setting", on_delete=models.CASCADE
    )
