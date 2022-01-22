from rest_framework import serializers

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay, Setting

class RoutineEveryDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineEveryDay
        fields = ("id", "name", "description", "start_time", "finish_time", "created_at", "updated_at")
        read_only_fields = ('created_at', 'updated_at')


class RoutineEveryWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineEveryWeek
        fields = ("id", "name", "description", "week", "start_time", "finish_time", "created_at", "updated_at")
        read_only_fields = ('created_at', 'updated_at')


class RoutineSpecDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineSpecDay
        fields = ("id", "name", "description", "date", "start_time", "finish_time", "created_at", "updated_at")
        read_only_fields = ('created_at', 'updated_at')


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ("id", "color")