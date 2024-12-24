from apiclient.discovery import build # type: ignore
from .models import APIkey

def youtube_search(query, max_results):
    """Fetch latest videos for a query using Youtube Data API.
    """
    api_keys = APIkey.objects.filter(is_limit_over=False)
    if not len(api_keys):
        return {}

    DEVELOPER_KEY = api_keys[0]

    try:
        search_keyword =build("youtube", "v3",developerKey=DEVELOPER_KEY).search().list(q=query, part="id, snippet",
                                                      maxResults=max_results).execute()
        results = search_keyword.get("items", [])
    except:
        api_keys[0].is_limit_over = True
        api_keys[0].save()
        return {}

    return results