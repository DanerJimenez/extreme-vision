from django.conf.urls import url

import server.controllers.GetAPI as GetAPI

urlpatterns = [
    url(r'^req/names/$', GetAPI.GetUsernames.as_view()),
]