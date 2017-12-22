from rest_framework import viewsets

from api.apps.stations.models import Station
from api.apps.stations.serializer import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()
