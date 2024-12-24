
from django.http import JsonResponse
from .models import Video

def get_most_recent_video(request):
    """Fetch the most recently added video from the database."""
    try:
        # Get the most recent video based on `created_at` timestamp
        most_recent_video = Video.objects.latest('created_at')
        
        # Prepare the video data as a dictionary
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
