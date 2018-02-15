from django.db import models
from django.db.models import CharField, DecimalField, ForeignKey

from api.models.geographical.places.models import Place


class Stop(models.Model):
    """
    Modelo para as paragens dos transportes públicos em Portugal

    Equivale ao stops.txt num feed GTFS
    """
    name = CharField(max_length=255, help_text="O campo de nome deve conter o nome de uma paragem.")
    latitude = DecimalField(max_digits=9, decimal_places=6,
                            help_text="O valor do campo deve ser uma latitude WGS 84 válida.")
    longitude = DecimalField(max_digits=9, decimal_places=6,
                            help_text="O valor do campo deve ser uma latitude WGS 84 válida.")
    place = ForeignKey(Place, models.DO_NOTHING, related_name='stops', null=True)

    def __str__(self):
        return self.name
