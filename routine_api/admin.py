from django.contrib import admin

from .models import RoutineEveryDay, RoutineEveryWeek, RoutineSpecDay, Setting

# Register your models here.
@admin.register(RoutineEveryDay)
class RoutineEveryDayAdmin(admin.ModelAdmin):
  pass

@admin.register(RoutineEveryWeek)
class RoutineEveryWeekAdmin(admin.ModelAdmin):
  pass

@admin.register(RoutineSpecDay)
class RoutineSpecDayAdmin(admin.ModelAdmin):
  pass

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
  pass