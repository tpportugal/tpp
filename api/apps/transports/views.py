from rest_framework import viewsets

from api.apps.transports.models import Transport
from api.apps.transports.serializer import TransportSerializer


class TransportViewSet(viewsets.ModelViewSet):
    serializer_class = TransportSerializer
    queryset = Transport.objects.all()
