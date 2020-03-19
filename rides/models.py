from django.conf import settings
from django.db import models

# Create your models here

class Route(models.Model):
    name = models.CharField(max_length=200, verbose_name="Route Name")
    world = models.CharField(max_length=200)
    length = models.FloatField(verbose_name="Length (km)")
    elevation = models.IntegerField(verbose_name="Elevation (m)")
    difficulty = models.FloatField()
    badgeXP = models.IntegerField(verbose_name="Badge XP")
    event = models.BooleanField()
    min_level = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
