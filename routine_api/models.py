from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_time = models.TimeField()
    finish_time = models.TimeField()


class RoutineEveryDay(Routine):
    pass


class RoutineEveryWeek(Routine):
    week = models.IntegerField()


class RoutineSpecDay(Routine):
    date = models.DateField()


class Setting(models.Model):
    color = models.CharField(max_length=8)
