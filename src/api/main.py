from fastapi import FastAPI, Query
from typing import Optional, List
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.models import WorkflowPopularity

app = FastAPI(
    title="n8n Workflow Popularity API",
    description="Aggregated popularity of n8n workflows from YouTube, Forum, and Google Trends",
    version="1.0.0",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/workflows")
def get_workflows(
    platform: Optional[str] = Query(None, description="YouTube | Forum | Google"),
    country: Optional[str] = Query(None, description="US | IN | Global"),
    sort_by: str = Query("views", description="views | likes | comments"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    db: Session = next(get_db())

    query = db.query(WorkflowPopularity)

    if platform:
        query = query.filter(WorkflowPopularity.platform == platform)

    if country:
        query = query.filter(WorkflowPopularity.country == country)

    if sort_by == "likes":
        query = query.order_by(WorkflowPopularity.likes.desc())
    elif sort_by == "comments":
        query = query.order_by(WorkflowPopularity.comments.desc())
    else:
        query = query.order_by(WorkflowPopularity.views.desc())

    results = query.offset(offset).limit(limit).all()

    return [
        {
            "workflow": r.workflow,
            "platform": r.platform,
            "views": r.views,
            "likes": r.likes,
            "comments": r.comments,
            "like_to_view_ratio": r.like_to_view_ratio,
            "comment_to_view_ratio": r.comment_to_view_ratio,
            "country": r.country,
            "source_url": r.source_url,
        }
        for r in results
    ]
@app.get("/")
def root():
    return {"status": "API is running"}
