from django.conf.urls import url

import server.controllers.GetAPI as GetAPI
import server.controllers.PostAPI as PostAPI

urlpatterns = [
    url(r'^req/names/$', GetAPI.GetUsernames.as_view()),
	url(r'^req/data/$', GetAPI.GetUserData.as_view()),
	
	url(r'^update/data/$', PostAPI.UpdateUserData.as_view()),
]