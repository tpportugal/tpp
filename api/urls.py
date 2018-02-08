from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from graphene_django.views import GraphQLView

from api import routers
from api.apps.communities import urls as communities_urls
from api.apps.companies import urls as companies_urls
from api.apps.gdrive.views import upload_timetable
from api.apps.schedules import urls as schedules_urls
from api.apps.stations import urls as stations_urls
from api.apps.transports import urls as transports_urls

router = routers.ApiRouter()
router.extend(communities_urls.router)
router.extend(companies_urls.router)
router.extend(schedules_urls.router)
router.extend(stations_urls.router)
router.extend(transports_urls.router)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^upload/', upload_timetable),
    url(r'^graphql/', GraphQLView.as_view(graphiql=True))
]
