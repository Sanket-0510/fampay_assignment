from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Video, APIkey
from .serializers import VideoSerializer, APIKeySerializer

class PaginatedVideoListView(APIView):
    """API to return videos in a paginated response sorted by publish datetime."""
    def get(self, request):
        videos = Video.objects.all().order_by('-pub_date')
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        result_page = paginator.paginate_queryset(videos, request)
        serializer = VideoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class APIKeyView(APIView):
    """API to add and view API keys."""
    
    def post(self, request):
        """Add a new API key."""
        serializer = APIKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)