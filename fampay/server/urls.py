from django.urls import path

from . import services
from . import views


urlpatterns = [
	path('getVideos', views.get_most_recent_video.as_view()),
]


services.THREAD.start()