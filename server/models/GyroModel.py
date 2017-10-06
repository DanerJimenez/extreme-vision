from django.db import models

class Gyro(models.Model) :
	x = models.DecimalField(max_digits=30, decimal_places=20)
	y = models.DecimalField(max_digits=30, decimal_places=20)
	z = models.DecimalField(max_digits=30, decimal_places=20)