from django.db import models
from django.db.models import CharField, ForeignKey, IntegerField

from api.models.gtfs.agencies.models import Agency


class Route(models.Model):
    """
    Modelo para as rotas dos transportes públicos em Portugal

    Equivale ao routes.txt num feed GTFS
    """

    TYPES = (
        (0, 'Trem'),
        (1, 'Metro'),
        (2, 'Comboio'),
        (3, 'Autocarro'),
        (4, 'Ferry'),
        (5, 'Elétrico'),
        (6, 'Teleférico'),
        (7, 'Funicular'),
    )

    short_name = CharField(max_length=20, help_text="O campo de nome deve conter o nome curto da rota.")
    long_name = CharField(max_length=255, help_text="O campo de nome deve conter o nome longo da rota.")
    type = IntegerField(help_text="O tipo de transporte usado na rota", choices=TYPES)
    agency = ForeignKey(Agency, models.DO_NOTHING, related_name='routes')

    def __str__(self):
        return "{0} - {1}".format(self.type, self.long_name)
