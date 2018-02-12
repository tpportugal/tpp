from django.db import models
from django.db.models import SlugField, CharField


class Agency(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)

    def __str__(self):
        return self.name
