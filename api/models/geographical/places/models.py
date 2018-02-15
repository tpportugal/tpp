from django.db import models
from django.db.models import SlugField, CharField, ForeignKey

from api.models.geographical.counties.models import County


class Place(models.Model):
    """
        Modelo para as localidades em Portugal
    """
    slug = SlugField()
    name = CharField(max_length=50)
    county = ForeignKey(County, models.DO_NOTHING, related_name='counties')

