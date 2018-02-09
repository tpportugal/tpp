from django.db import models
from django.forms import FileInput

from api.apps.companies.models import Company


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='maps', verbose_name="Ficheiro", widget=FileInput(attrs={'accept':'application/pdf,image/jpeg,image/png'}))
    # Training Data
    company = models.ForeignKey(Company, models.DO_NOTHING)
