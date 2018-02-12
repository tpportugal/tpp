from django.db import models
from django.db.models import SlugField, CharField, ForeignKey

from api.apps.geographical.districts.models import District


class City(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)
    district = ForeignKey(District, models.DO_NOTHING, related_name='cities')
