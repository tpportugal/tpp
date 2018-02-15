from django.db import models
from django.db.models import SlugField, CharField, ForeignKey

from api.models.geographical.districts.models import District


class County(models.Model):
    """
        Modelo para os concelhos em Portugal
    """
    slug = SlugField()
    name = CharField(max_length=50)
    district = ForeignKey(District, models.DO_NOTHING, related_name='counties')

    class Meta:
        verbose_name_plural = "counties"
