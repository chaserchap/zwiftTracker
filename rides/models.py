from django.conf import settings
from django.db import models

# Create your models here

class Route(models.Model):
	name = models.CharField(max_length=200)
	world = models.CharField(max_length=200)
	length = models.FloatField()
	elevation = models.IntegerField()
	difficulty = models.FloatField()
	badgeXP = models.IntegerField()
	event = models.BooleanField()
	min_level = models.IntegerField(default=0)
