from django.contrib import admin

from .models import Stoptime


@admin.register(Stoptime)
class StoptimeAdmin(admin.ModelAdmin):
    list_display = ['trip', 'stop', 'stop_sequence', 'arrival_time', 'departure_time']
