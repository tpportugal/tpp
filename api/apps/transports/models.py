from django.db import models
from django.db.models import SlugField, CharField, ForeignKey

from api.apps.companies.models import Company
from api.apps.schedules.models import Schedule


class Transport(models.Model):
    TRANSPORT_CHOICES = (
        (0, 'Train'),
        (1, 'Metro')
    )
    slug = SlugField()
    name = CharField(max_length=50)
    company = ForeignKey(Company, models.DO_NOTHING)
    type = CharField(max_length=50, choices=TRANSPORT_CHOICES)
    schedule = ForeignKey(Schedule, models.DO_NOTHING)