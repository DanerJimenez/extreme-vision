import json

import django.views as views

from django.http import JsonResponse
from django.core import serializers

		
class GetUsernames(views.View) :
	
	def get(self, request) :
		json_response = {
			"usernames" : [
				"testuser1",
				"testuser2"
			]
		}

		return JsonResponse(json_response)
		
	
class GetUserData(views.View) :
	
	def get(self, request) :
		username = request.GET.get('username')
		
		if username == 'testuser1' :
			json_response = {
				'status' : 0,
				
				'gps' : {
					'x' : 1.0,
					'y' : 2.0
				},
				
				'gyro' : {
					'x' : 3.0,
					'y' : 4.0,
					'z' : 5.0
				},
				
				'accel' : {
					'x' : 6.0,
					'y' : 7.0,
					'z' : 8.0
				}
			}
			
			return JsonResponse(json_response)
			
		elif username == 'testuser2' :	
			json_response = {
				'status' : 0,
				
				'gps' : {
					'x' : 1.1,
					'y' : 2.2
				},
				
				'gyro' : {
					'x' : 3.3,
					'y' : 4.4,
					'z' : 5.5
				},
				
				'accel' : {
					'x' : 6.6,
					'y' : 7.7,
					'z' : 8.8
				}
			}
			
			return JsonResponse(json_response)
			
		else :
			return JsonResponse({'status' : 1})
