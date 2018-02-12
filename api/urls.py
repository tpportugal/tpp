from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from graphene_django.views import GraphQLView
from api.apps.gdrive.views import upload_timetable


urlpatterns = [
    url(r'^api/', GraphQLView.as_view(graphiql=getattr(settings, "GRAPHQL_EDITOR", False))),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', upload_timetable),
]
