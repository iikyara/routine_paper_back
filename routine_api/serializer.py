from rest_framework import serializers

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay, Setting


class RoutineEveryDaySerializer(serializers.ModelSerializer):
  class Meta:
    model = RoutineEveryDay
    fields = "__all__"

class RoutineEveryWeekSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoutineEveryWeek
    fields = "__all__"

class RoutineSpecDaySerializer(serializers.ModelSerializer):
  class Meta:
    model = RoutineSpecDay
    fields = "__all__"

class SettingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Setting
    fields = "__all__"