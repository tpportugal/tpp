from django.contrib import admin

from api.models.agencies.models import Agency


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
