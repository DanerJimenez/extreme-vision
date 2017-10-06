import django.views as views
import json
from django.http import JsonResponse
from django.core import serializers


class GetWholeDatabase(views.View) :
	
	def get(self, request) :
#		json_response = {
		json_response =	'{\
			"usernames" : [\
				"testuser1",\
				"testuser2"\
			]\
		}'
		return JsonResponse( 
			json.loads(json_response)
		)
		
		
class GetUsernames(views.View) :
	
	def get(self, request) :
		json_response = {
			"usernames" : [
				"testuser1",
				"testuser2"
			]
		}

		return JsonResponse( 
			json_response
		)
		
	