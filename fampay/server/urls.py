from django.urls import path
from . import views


urlpatterns = [
	path('getVideos', views.PaginatedVideoListView.as_view(), name='paginated_videos'),
    path('searchVideos', views.OptimizedSearchVideo.as_view(), name="view_for_searching_videos"),
    path('addApiKey', views.APIKeyView.as_view(), name="api_to_add_new_youtube_api_key")
]


