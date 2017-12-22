from rest_framework import serializers

from api.apps.stations.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        depth = 1
        fields = '__all__'
