from rest_framework import routers

from api.apps.schedules.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'schedules', ScheduleViewSet)
