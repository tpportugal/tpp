from django.db import models
from django.db.models import ForeignKey, PositiveIntegerField, TimeField

from api.models.gtfs.stops.models import Stop
from api.models.gtfs.trips.models import Trip


class Stoptime(models.Model):
    """
    Modelo para os horários dos transportes públicos em Portugal

    Equivale ao stop_times.txt num feed GTFS
    """

    trip = ForeignKey(Trip, models.DO_NOTHING, related_name='stoptimes')
    stop = ForeignKey(Stop, models.DO_NOTHING, related_name='stoptimes')
    stop_sequence = PositiveIntegerField(default=1)
    arrival_time = TimeField()
    departure_time = TimeField()
