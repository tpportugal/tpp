from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from graphene_django.views import GraphQLView
from api.models.gdrive.views import upload_timetable


urlpatterns = [
    url(r'^api/', GraphQLView.as_view(graphiql=getattr(settings, "GRAPHQL_EDITOR", False))),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', upload_timetable),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
