from __future__ import unicode_literals

from django.db import models


class Vehicles(models.Model):
    reg_num=models.CharField(max_length=10,blank=False)
    lat = models.CharField(max_length=8, blank=False)
    lont = models.CharField(max_length=8, blank=False)
    ign_status = models.CharField(max_length=8, blank=False)
    fuel_lvl = models.CharField(max_length=8, blank=False)
    tmstmp=models.CharField(max_length=20,blank=False)

    objects = models.Manager()

