import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def fetch_n8n_workflow_videos(max_results: int = 5):
    """
    Fetch n8n-related YouTube videos and return basic stats
    """

    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part="snippet",
        q="n8n workflow automation",
        type="video",
        maxResults=max_results,
    )
    response = request.execute()

    videos = []

    for item in response.get("items", []):
        video_id = item["id"]["videoId"]

        stats_request = youtube.videos().list(
            part="statistics,snippet",
            id=video_id,
        )
        stats_response = stats_request.execute()

        stats = stats_response["items"][0]["statistics"]
        snippet = stats_response["items"][0]["snippet"]

        videos.append(
            {
                "workflow": snippet["title"],
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
                "source_url": f"https://www.youtube.com/watch?v={video_id}",
            }
        )

    return videos


def extract_workflow_popularity_data(video: dict) -> dict:
    """
    Normalize YouTube video data into workflow popularity schema
    """

    views = video.get("views", 0)
    likes = video.get("likes", 0)
    comments = video.get("comments", 0)

    return {
        "workflow": video.get("workflow"),
        "platform": "YouTube",
        "views": views,
        "likes": likes,
        "comments": comments,
        "like_to_view_ratio": round(likes / views, 4) if views > 0 else 0,
        "comment_to_view_ratio": round(comments / views, 4) if views > 0 else 0,
        "country": "US",
        "source_url": video.get("source_url"),
    }
