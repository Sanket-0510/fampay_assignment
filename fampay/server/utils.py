from django.shortcuts import render
import asyncio
from datetime import datetime
from .models import Video, APIkey
from .youtube_api import youtube_search
import threading
from asgiref.sync import sync_to_async
from googleapiclient.discovery import build

async def search_and_add_youtube_videos():
    """Fetch and store the latest videos."""
    print("Fetching YouTube videos...")

    api_keys = await sync_to_async(list)(APIkey.objects.filter(is_key_exhausted=False))
    
    if not api_keys:
        print("No valid API keys available.")
        return

    search_results = await sync_to_async(youtube_search)('startup news', 10)

    if search_results:
        for result in search_results:
            if 'videoId' in result['id']:
                video_id = result['id']['videoId']
            else:
                video_id = ''
            title = result['snippet']['title']
            description = result['snippet']['description']
            publish_date_time = result['snippet']['publishedAt']
            channel_id = result['snippet']['channelId']
            channel_title = result['snippet']['channelTitle']
            thumbnails = result['snippet'].get('thumbnails', {})
            thumbnail_url = thumbnails.get('default', {}).get('url', '')

            publish_date_time_obj = datetime.strptime(publish_date_time, "%Y-%m-%dT%H:%M:%SZ")

            video_exists = await sync_to_async(Video.objects.filter(video_id=video_id).exists)()
            if not video_exists:
                # Save the video details to the database
                await sync_to_async(Video.objects.create)(
                    video_id=video_id,
                    video_title=title,
                    video_description=description,
                    pub_date=publish_date_time_obj,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    thumb_url=thumbnail_url,
                )
                print(f"Added video: {title}")
    else:
        print("No search results returned.")


async def periodic_search_youtube_videos():
    """Asynchronous periodic service to search and add YouTube videos every 10 seconds."""
    print("Started periodic search and add service...")
    while True:
        try:
            await search_and_add_youtube_videos()
        except Exception as e:
            print(f"Error in search_and_add_youtube_videos_service: {e}")
        await asyncio.sleep(10)  


def start_adding_youtube_videos():
    """Start the background service using a thread."""
    def run_event_loop():
        asyncio.run(periodic_search_youtube_videos())

    thread = threading.Thread(target=run_event_loop, daemon=True)
    thread.start()
    print("Background thread started for periodic video fetching.")
