import json

import django.views as views

from django.http import JsonResponse
from django.core import serializers

import server.source.db.interface.Database as Database
		
class UpdateUserData(views.View) :
	
	def post(self, request) :
		latitude = request.GET.get('latitude')
		longitude = request.GET.get('longitude')
		
		return JsonResponse(json_response)
