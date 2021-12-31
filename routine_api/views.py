from rest_framework import viewsets

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay, Setting
from .serializer import (
    RoutineEveryDaySerializer,
    RoutineEveryWeekSerializer,
    RoutineSpecDaySerializer,
    SettingSerializer,
)


class RoutineEveryDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineEveryDay.objects.all()
    serializer_class = RoutineEveryDaySerializer


class RoutineEveryWeekViewSet(viewsets.ModelViewSet):
    queryset = RoutineEveryWeek.objects.all()
    serializer_class = RoutineEveryWeekSerializer


class RoutineSpecDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineSpecDay.objects.all()
    serializer_class = RoutineSpecDaySerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
