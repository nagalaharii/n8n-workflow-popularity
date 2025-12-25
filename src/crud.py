from sqlalchemy.orm import Session
from datetime import datetime

from src.models import WorkflowPopularity
from src.database import SessionLocal


def create_workflow_popularity(
    db: Session,
    workflow: str,
    platform: str,
    views: int,
    likes: int,
    comments: int,
    country: str,
    source_url: str,
):
    like_to_view_ratio = likes / views if views else 0
    comment_to_view_ratio = comments / views if views else 0

    db_record = WorkflowPopularity(
        workflow=workflow,
        platform=platform,
        views=views,
        likes=likes,
        comments=comments,
        like_to_view_ratio=like_to_view_ratio,
        comment_to_view_ratio=comment_to_view_ratio,
        country=country,
        source_url=source_url,
        last_updated=datetime.utcnow(),
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
