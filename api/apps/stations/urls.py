from rest_framework import routers

from api.apps.stations.views import StationViewSet

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
