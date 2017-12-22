from rest_framework import serializers

from api.apps.transports.models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        depth = 1
        fields = '__all__'
