from django.contrib import admin

from .models import CalendarDate


@admin.register(CalendarDate)
class CalendarDateAdmin(admin.ModelAdmin):
    list_display = ['service', 'date', 'exception_type']
