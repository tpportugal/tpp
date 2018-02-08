from django.contrib import admin

from api.apps.cities.models import City
from api.apps.gdrive.models import Timetable


@admin.register(Timetable)
class GdriveAdmin(admin.ModelAdmin):
    list_display = ['company', 'map_data']
