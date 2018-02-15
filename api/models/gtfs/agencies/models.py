from django.db import models
from django.db.models import SlugField, CharField, URLField


class Agency(models.Model):
    """
    Modelo para as operadores de transportes públicos em Portugal

    Equivale ao agency.txt num feed GTFS
    """
    slug = SlugField()
    name = CharField(max_length=50, db_index=True, help_text="Nome completo da operadora de transportes")
    url = URLField(blank=True, help_text="URL da operadora de transportes")
    # Lista de Timezone válidas --> http://en.wikipedia.org/wiki/List_of_tz_zones
    timezone = CharField(max_length=255, help_text="Timezone da opderadora de transportes", default="Europe/Lisbon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "agencies"
