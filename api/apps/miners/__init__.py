from django.db import models
from django.db.models import ForeignKey, TextField

from api.apps.companies.models import Company


class Miner(models.Model):
    company = ForeignKey(Company, models.DO_NOTHING)
    endpoint = TextField()
