from rest_framework import serializers

from api.apps.communities.models import Community


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        depth = 1
        fields = '__all__'
