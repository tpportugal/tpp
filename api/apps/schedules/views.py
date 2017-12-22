from rest_framework import viewsets

from api.apps.schedules.models import Schedule
from api.apps.schedules.serializer import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
