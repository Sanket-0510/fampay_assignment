from django.urls import path
from . import views


urlpatterns = [
	path('getVideos', views.PaginatedVideoListView.as_view(), name='paginated_videos'),
    path('serchVideos', views.OptimizedSearchVideo.as_view(), name="view_for_searching_videos")
]


