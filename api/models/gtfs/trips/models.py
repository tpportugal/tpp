from django.db import models
from django.db.models import ForeignKey

from api.models.gtfs.routes.models import Route
from api.models.gtfs.calendardates.models import CalendarDate


class Trip(models.Model):
    """
    Modelo para as viagens dos transportes públicos em Portugal

    Equivale ao trips.txt num feed GTFS
    """

    route = ForeignKey(Route, models.DO_NOTHING, related_name='trips')
    calendardate = ForeignKey(CalendarDate, models.DO_NOTHING, related_name='trips')
