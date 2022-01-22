from os import O_WRONLY
from django_filters import rest_framework as filters

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay

class RoutineEveryDayFilter(filters.FilterSet):
  id = filters.UUIDFilter()
  name = filters.CharFilter(field_name="name", lookup_expr="contains")

  class Meta:
    model = RoutineEveryDay
    fields = ()

class RoutineEveryWeekFilter(filters.FilterSet):
  id = filters.UUIDFilter()
  routine_name = filters.CharFilter(field_name="name", lookup_expr="contains")
  week = filters.ChoiceFilter(field_name="week", choices=RoutineEveryWeek.WEEK_SET)

  class Meta:
    model = RoutineEveryWeek
    fields = ()

class RoutineSpecDayFilter(filters.FilterSet):
  id = filters.UUIDFilter()
  routine_name = filters.CharFilter(field_name="name", lookup_expr="contains")
  date = filters.DateFilter(field_name="date")
  date_from = filters.DateFilter(field_name="date", lookup_expr="gte")
  date_to = filters.DateFilter(field_name="date", lookup_expr="lte")

  class Meta:
    model = RoutineSpecDay
    fields = ()