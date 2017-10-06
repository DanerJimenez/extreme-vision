from django.contrib import admin

from server.models.UserModel import User
from server.models.GpsModel import Gps
from server.models.GyroModel import Gyro
from server.models.AccelModel import Accel

admin.site.register(User)
admin.site.register(Gps)
admin.site.register(Accel)
admin.site.register(Gyro)


# Register your models here.
