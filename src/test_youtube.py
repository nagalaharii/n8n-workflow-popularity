from src.youtube_fetcher import fetch_n8n_workflow_videos

videos = fetch_n8n_workflow_videos(max_results=5)

for video in videos:
    print(video)
