
from django.http import JsonResponse
from .models import Video,APIkey

def get_most_recent_video(request):
    """Fetch the most recently added video from the database."""
    try:
        most_recent_video = Video.objects.latest('created_at')
        video_data = {
            'video_id': most_recent_video.video_id,
            'video_title': most_recent_video.video_title,
            'video_description': most_recent_video.video_description,
            'pub_date': most_recent_video.pub_date,
            'channel_id': most_recent_video.channel_id,
            'channel_title': most_recent_video.channel_title,
            'thumb_url': most_recent_video.thumb_url,
        }
        return JsonResponse({'status': 'success', 'video': video_data})
    except Video.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'No videos found'}, status=404)


