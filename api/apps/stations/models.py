from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import SlugField, CharField, IntegerField


class Station(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)
    longitude_degree = IntegerField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    longitude_minutes = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    longitude_seconds = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    latitude_degree = IntegerField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    latitude_minutes = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    latitude_seconds = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
