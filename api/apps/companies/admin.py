from django.contrib import admin

from api.apps.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
