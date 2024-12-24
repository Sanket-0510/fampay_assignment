from django.urls import path

from . import services
from . import views


urlpatterns = [
	path('getVideos', views.PaginatedVideoListView.as_view(), name='paginated_videos'),
]


