from django.contrib import admin

from api.apps.cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'district']
