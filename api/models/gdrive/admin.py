from django.contrib import admin

from api.models.gdrive.models import Timetable


@admin.register(Timetable)
class GdriveAdmin(admin.ModelAdmin):
    list_display = ['agency', 'map_data']
