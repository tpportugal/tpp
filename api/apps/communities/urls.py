from rest_framework import routers

from api.apps.communities.views import CommunityViewSet

router = routers.DefaultRouter()
router.register(r'communities', CommunityViewSet)
