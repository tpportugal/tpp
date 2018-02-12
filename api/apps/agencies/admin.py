from django.contrib import admin

from api.apps.agencies.models import Agency


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
