from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Video, APIkey
from .serializers import VideoSerializer, APIKeySerializer
from django.db.models import Q

class PaginatedVideoListView(APIView):
    """API to return videos in a paginated response sorted by publish datetime."""
    def get(self, request):
        videos = Video.objects.all().order_by('-pub_date')
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        result_page = paginator.paginate_queryset(videos, request)
        serializer = VideoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    
class OptimizedSearchVideo(APIView):
    """API for searching videos by title or description with partial matching."""

    def get(self, request):
        search_query = request.query_params.get('query', '')

        if search_query:
            videos = Video.objects.filter(
                Q(video_title__icontains=search_query) | Q(video_description__icontains=search_query)
            ).order_by('-pub_date') 
        else:
            videos = Video.objects.all().order_by('-pub_date')
        serializer = VideoSerializer(videos, many=True)
        return Response({'status': 'success', 'data': serializer.data})
    

class APIKeyView(APIView):
    """API to add and view API keys."""

    def post(self, request):
        """Add a new API key."""
        serializer = APIKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)