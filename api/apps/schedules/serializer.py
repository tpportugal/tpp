from rest_framework import serializers

from api.apps.schedules.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        depth = 1
        fields = '__all__'
