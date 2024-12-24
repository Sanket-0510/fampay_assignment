from django.shortcuts import render
import time
# Create your views here.
import asyncio
from datetime import datetime
from .models import Video, APIkey
from .youtube_api import youtube_search

import asyncio
import threading

async def search_and_add_youtube_videos_service():
    """Fetch and store latest videos every 10 seconds."""
    while True:
        search_results = youtube_search('today news', 10)

        if search_results:
          for result in search_results:
              video_id = result['id']['videoId']
              title = result['snippet']['title']
              description = result['snippet']['description']
              publish_date_time = result['snippet']['publishedAt']
              channel_id = result['snippet']['channelId']
              channel_title = result['snippet']['channelTitle']  
              thumbnails = result['snippet'].get('thumbnails', {})
              thumbnail_url = thumbnails.get('default', {}).get('url', '')
              publish_date_time_obj = datetime.strptime(publish_date_time, "%Y-%m-%dT%H:%M:%SZ")
      
              if not Video.objects.filter(video_id=video_id).exists():
                  Video.objects.create(
                      video_id=video_id,
                      video_title=title,
                      video_description=description,
                      pub_date=publish_date_time_obj,
                      channel_id=channel_id,
                      channel_title=channel_title,
                      thumb_url=thumbnail_url,
                  )
        await asyncio.sleep(10)  



def start_searching_and_adding_youtube_videos():
    """Start background service to search and add YouTube videos every 10 seconds."""
    while True:
        api_keys = APIkey.objects.filter(is_limit_over=False)
        if api_keys:
            asyncio.run(search_and_add_youtube_videos_service())
        time.sleep(10)  


video_fetch_thread = threading.Thread(target=start_searching_and_adding_youtube_videos)
video_fetch_thread.start()