from rest_framework import routers
from .views import RoutineEveryDayViewSet, RoutineEveryWeekViewSet, RoutineSpecDayViewSet, SettingViewSet


router = routers.DefaultRouter()
router.register(r"everyday", RoutineEveryDayViewSet)
router.register(r"everyweek", RoutineEveryWeekViewSet)
router.register(r"specday", RoutineSpecDayViewSet)
router.register(r"setting", SettingViewSet)
