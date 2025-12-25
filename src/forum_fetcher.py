import requests


BASE_URL = "https://community.n8n.io"


def fetch_forum_workflows(limit: int = 10):
    """
    Fetch popular topics from n8n Discourse forum
    """
    url = f"{BASE_URL}/latest.json"
    response = requests.get(url)
    response.raise_for_status()

    topics = response.json()["topic_list"]["topics"]
    workflows = []

    for topic in topics[:limit]:
        workflows.append(
            {
                "workflow": topic["title"],
                "platform": "Forum",
                "views": topic.get("views", 0),
                "likes": topic.get("like_count", 0),
                "comments": topic.get("posts_count", 0),
                "like_to_view_ratio": (
                    round(topic.get("like_count", 0) / topic["views"], 4)
                    if topic.get("views", 0) > 0
                    else 0
                ),
                "comment_to_view_ratio": (
                    round(topic.get("posts_count", 0) / topic["views"], 4)
                    if topic.get("views", 0) > 0
                    else 0
                ),
                "country": "Global",
                "source_url": f"{BASE_URL}/t/{topic['slug']}/{topic['id']}",
            }
        )

    return workflows
