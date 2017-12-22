from rest_framework import viewsets

from api.apps.communities.models import Community
from api.apps.communities.serializer import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    serializer_class = CommunitySerializer
    queryset = Community.objects.all()
