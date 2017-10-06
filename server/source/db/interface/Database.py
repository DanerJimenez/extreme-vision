from server.models.UserModel import User

def getUsernames() :
	username_db = {
		"usernames" : list(User.objects.all().values_list('username', flat=True))
	}
	return username_db

def getUserData(username) :
	user = User.objects.filter(username=username)	
	if user is None :
		return {'status' : 1}
	else :
		return user[0].toJson()
		
def updateData(request) :
	username = request.get('username')
	user = User.objects.filter(username=username)[0]	
	if user is not None :
		updateFieldsOf(user, request)
		
def updateFieldsOf(user, request) :
	latitude = request.get('latitude')
	if latitude is not None :
		user.gps.y = latitude
	
	longitude = request.get('longitude')
	if longitude is not None :
		user.gps.x = longitude
	
	user.saveAll()