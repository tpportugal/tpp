from django.db import models
from django.db.models import CharField, SlugField


class Schedule(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)
