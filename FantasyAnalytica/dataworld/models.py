from django.db import models
from . import league
# Create your models here.


class dataworld(models.Model):
    title = models.Charfield(max_length=200)