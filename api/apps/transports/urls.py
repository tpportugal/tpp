from rest_framework import routers

from api.apps.transports.views import TransportViewSet

router = routers.DefaultRouter()
router.register(r'transports', TransportViewSet)
