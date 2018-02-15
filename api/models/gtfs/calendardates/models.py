from django.db import models
from django.db.models import ForeignKey, IntegerField, DateField

from api.models.gtfs.services.models import Service


class CalendarDate(models.Model):
    """
    Modelo para as datas de calendário dos transportes públicos em Portugal

    Equivale ao calendar_dates.txt num feed GTFS
    """

    EXCEPTION_TYPES = (
        (1, 'Serviço adicionado'),
        (2, 'Serviço removido'),
    )

    service = ForeignKey(Service, models.DO_NOTHING, related_name='calendardates')
    date = DateField(null=True)
    exception_type = IntegerField(choices=EXCEPTION_TYPES)

    def __str__(self):
        return "{0} - {1}".format(self.service, self.exception_type)
