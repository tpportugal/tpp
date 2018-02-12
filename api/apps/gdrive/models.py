from django.db import models

from api.apps.agencies.models import Agency


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='maps', verbose_name="Ficheiro")
    # Training Data
    agency = models.ForeignKey(Agency, models.DO_NOTHING)
