import json

import django.views as views

from django.http import JsonResponse
from django.core import serializers

import server.source.db.interface.Database as Database
		
class GetUsernames(views.View) :
	
	def get(self, request) :
		json_response = Database.getUsernames()
		return JsonResponse(json_response)
		
	
class GetUserData(views.View) :
	
	def get(self, request) :
		username = request.GET.get('username')
		json_response = Database.getUserData(username)	
		return JsonResponse(json_response)
