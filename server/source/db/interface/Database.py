
from server.models.UserModel import User
from server.models.GpsModel import Gps

def getUsernames() :
	username_db = {
		"usernames" : 
		[
			"mark",
			"matthew",
			"luke",
			"john"
		]
	}
	return username_db

def getUserData(username) :

	json_response = {'status' : 1}
	if username == 'mark' :
		json_response = {
			'status' : 0,
			
			'gps' : {
				'x' : 121.0541,
				'y' : 14.6578
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
	
	elif username == 'matthew' :	
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
		
	return json_response
	