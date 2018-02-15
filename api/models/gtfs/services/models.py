from django.db import models
from django.db.models import BinaryField, DateField


class Service(models.Model):
    """
    Modelo para os serviços dos transportes públicos em Portugal

    Equivale ao services.txt num feed GTFS
    """

    monday = BinaryField(default=0)
    tuesday = BinaryField(default=0)
    wednesday = BinaryField(default=0)
    thursday = BinaryField(default=0)
    friday = BinaryField(default=0)
    saturday = BinaryField(default=0)
    sunday = BinaryField(default=0)
    start_date = DateField()
    end_date = DateField()
