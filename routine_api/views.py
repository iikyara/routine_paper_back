from django_filters import rest_framework as filters
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay, Setting
from .serializer import (
    RoutineEveryDaySerializer,
    RoutineEveryWeekSerializer,
    RoutineSpecDaySerializer,
    SettingSerializer,
)
from .permission import IsOwnerPermission
from .filter import RoutineEveryDayFilter, RoutineEveryWeekFilter, RoutineSpecDayFilter


class RoutineEveryDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineEveryDay.objects.all()
    serializer_class = RoutineEveryDaySerializer
    permission_classes = (IsOwnerPermission,)
    filter_class = RoutineEveryDayFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class RoutineEveryWeekViewSet(viewsets.ModelViewSet):
    queryset = RoutineEveryWeek.objects.all()
    serializer_class = RoutineEveryWeekSerializer
    permission_classes = (IsOwnerPermission,)
    filter_class = RoutineEveryWeekFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class RoutineSpecDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineSpecDay.objects.all()
    serializer_class = RoutineSpecDaySerializer
    permission_classes = (IsOwnerPermission,)
    filter_class = RoutineSpecDayFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (IsOwnerPermission,)

    def perform_create(self, serializer):
        queryset = Setting.objects.filter(owner=self.request.user)
        if queryset.exists():
            raise ValidationError("You have already setting data.")
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
