from django.db import models

from server.models.GpsModel import Gps

class User(models.Model) :
	username = models.CharField(max_length = 30)
	gps = models.ForeignKey(Gps, on_delete = models.CASCADE, null = True)
	