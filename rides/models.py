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

class Ride(models.Model):
    route = models.ForeignKey(Route, on_delete=models.SET_DEFAULT, default="Unknown")
    ride_time = models.FloatField(verbose_name="Total Time")
    active_time = models.FloatField(verbose_name="Active Time")
    date = models.DateField()
    max_power = models.IntegerField(verbose_name="Max Power")
    avg_power = models.IntegerField(verbose_name="Average Power")
    max_hr = models.IntegerField(verbose_name="Max Heartrate")
    avg_hr = models.IntegerField(verbose_name="Average Heartrate")
    act_dist = models.FloatField(verbose_name="Actual Distance (m)")
    calories = models.IntegerField()
    total_work = models.IntegerField(verbose_name="Total Work (kJ)")
    avg_cadence = models.IntegerField(verbose_name="Average Cadence")
    max_cadence = models.IntegerField(verbose_name="Max Cadence")
    act_elevation = models .IntegerField(verbose_name="Actual Elevation Gain (m)")
    avg_spd = models.FloatField(verbose_name="Average Speed (kph)")
    max_spd = models.FloatField(verbose_name="Maximum Speed (kph)")
