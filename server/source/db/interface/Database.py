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