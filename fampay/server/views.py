from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer

class PaginatedVideoListView(APIView):
    """API to return videos in a paginated response sorted by publish datetime."""
    def get(self, request):
        videos = Video.objects.all().order_by('-pub_date')
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        result_page = paginator.paginate_queryset(videos, request)
        serializer = VideoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
