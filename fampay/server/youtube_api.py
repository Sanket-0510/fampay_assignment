from googleapiclient.discovery import build
from .models import APIkey


def youtube_search(query, max_results):
    """
    Fetch latest videos for a query using the YouTube Data API.
    """
    api_keys = APIkey.objects.filter(is_key_exhausted=False)
    if not api_keys.exists():
        print("No available API keys.")
        return []
    api_key_instance = api_keys.first()
    DEVELOPER_KEY = api_key_instance.key  

    try:
        youtube_client = build("youtube", "v3", developerKey=DEVELOPER_KEY)
        search_keyword = youtube_client.search().list(
            q=query,
            part="id,snippet",
            maxResults=max_results
        ).execute()
    
        results = search_keyword.get("items", [])
        return results

    except Exception as e:
        print(f"Error using API key {DEVELOPER_KEY}: {e}")
        api_key_instance.is_key_exhausted = True
        api_key_instance.save()
        return []