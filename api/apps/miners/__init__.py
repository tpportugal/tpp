from django.db import models
from django.db.models import ForeignKey, TextField

from api.apps.agencies.models import Agency


class Miner(models.Model):
    agency = ForeignKey(Agency, models.DO_NOTHING)
    endpoint = TextField()
