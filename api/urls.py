from django.conf.urls import url
from django.contrib import admin
from graphene_django.views import GraphQLView
from api.apps.gdrive.views import upload_timetable


urlpatterns = [
    url(r'^', GraphQLView.as_view(graphiql=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', upload_timetable),
]
