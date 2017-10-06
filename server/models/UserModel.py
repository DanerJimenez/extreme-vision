from django.db import models

from server.models.GpsModel import Gps
from server.models.GyroModel import Gyro
from server.models.AccelModel import Accel

class User(models.Model) :
	username = models.CharField(max_length = 30)
	gps = models.ForeignKey(Gps, on_delete = models.CASCADE, null = True)
	accel = models.ForeignKey(Accel, on_delete = models.CASCADE, null = True)
	gyro = models.ForeignKey(Gyro, on_delete = models.CASCADE, null = True)
	
	def toJson(self) :
		return {
			'gps' : self.gps.toJson(),
			'accel' : self.accel.toJson(),
			'gyro' : self.gyro.toJson()
		}
		
	def saveAll(self) :
		self.gps.save()
		self.accel.save()
		self.gyro.save()
		self.save()