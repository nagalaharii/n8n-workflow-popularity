# Fetch popular n8n workflows from Discourse forum
# Use topics API to get replies, likes, views, contributors
import os
import requests
DISCOURSE_API_URL = os.getenv("DISCOURSE_API_URL", "https://forum.n8n.io")
DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.getenv("DISCOURSE_API_USERNAME", "system")
def fetch_popular_workflow_topics(min_replies=5, min_likes=10):
    topics_url = f"{DISCOURSE_API_URL}/latest.json"
    headers = {
        "Api-Key": DISCOURSE_API_KEY,
        "Api-Username": DISCOURSE_API_USERNAME,
    }
    params = {
        "limit": 100,
    }
    response = requests.get(topics_url, headers=headers, params=params)
    response.raise_for_status()
    topics = response.json().get("topics", [])
    popular_topics = [
        topic for topic in topics
        if topic.get("reply_count", 0) >= min_replies and
           topic.get("like_count", 0) >= min_likes
    ]
    return popular_topics
def extract_workflow_popularity_data(topic):
    replies = topic.get("reply_count", 0)
    likes = topic.get("like_count", 0)
    views = topic.get("views", 0)
    contributors = topic.get("posts_count", 0)  # Approximation
    like_to_view_ratio = (likes / views) if views > 0 else 0
    reply_to_view_ratio = (replies / views) if views > 0 else 0
    return {
        "topic_id": topic["id"],
        "title": topic["title"],
        "replies": replies,
        "likes": likes,
        "views": views,
        "contributors": contributors,
        "like_to_view_ratio": like_to_view_ratio,
        "reply_to_view_ratio": reply_to_view_ratio,
        "source_url": f"{DISCOURSE_API_URL}/t/{topic['slug']}/{topic['id']}",
    }
# Example usage:
if __name__ == "__main__":
    popular_topics = fetch_popular_workflow_topics()
    for topic in popular_topics:
        popularity_data = extract_workflow_popularity_data(topic)
        print(popularity_data)
        