import json

import django.views as views

from django.http import JsonResponse
from django.core import serializers

import server.source.db.interface.Database as Database
		
class UpdateUserData(views.View) :
	
	def get(self, request) :
		Database.updateData(request.GET)
		return JsonResponse({'status' : 'ok'})
