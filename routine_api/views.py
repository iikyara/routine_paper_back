from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = (IsAuthenticated,)


class RoutineEveryWeekViewSet(viewsets.ModelViewSet):
    queryset = RoutineEveryWeek.objects.all()
    serializer_class = RoutineEveryWeekSerializer
    permission_classes = (IsAuthenticated,)


class RoutineSpecDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineSpecDay.objects.all()
    serializer_class = RoutineSpecDaySerializer
    permission_classes = (IsAuthenticated,)


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (IsAuthenticated,)
