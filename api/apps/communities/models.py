from django.db import models
from django.db.models import SlugField, ForeignKey, CharField

from api.apps.cities.models import City


class Community(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)
    city = ForeignKey(City, models.DO_NOTHING)
