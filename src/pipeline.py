from datetime import datetime

from src.database import SessionLocal
from src.models import WorkflowPopularity
from src.youtube_fetcher import (
    fetch_n8n_workflow_videos,
    extract_workflow_popularity_data,
)
from src.forum_fetcher import fetch_forum_workflows
from src.google_trends_fetcher import fetch_google_trends_workflows


def upsert(db, data: dict):
    existing = (
        db.query(WorkflowPopularity)
        .filter(WorkflowPopularity.source_url == data["source_url"])
        .first()
    )

    if existing:
        for key, value in data.items():
            setattr(existing, key, value)
        existing.last_updated = datetime.utcnow()
    else:
        record = WorkflowPopularity(**data)
        db.add(record)


def run_pipeline():
    db = SessionLocal()

    # ---- YouTube ----
    youtube_videos = fetch_n8n_workflow_videos(max_results=5)
    for video in youtube_videos:
        data = extract_workflow_popularity_data(video)
        upsert(db, data)

    # ---- Forum ----
    forum_workflows = fetch_forum_workflows(limit=10)
    for data in forum_workflows:
        upsert(db, data)

    # ---- Google Trends ----
    google_workflows = fetch_google_trends_workflows(country="US")
    for data in google_workflows:
        upsert(db, data)

    db.commit()
    db.close()
    print("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
