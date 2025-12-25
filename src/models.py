from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class WorkflowPopularity(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    workflow = Column(String, index=True)
    platform = Column(String, index=True)
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    like_to_view_ratio = Column(Float)
    comment_to_view_ratio = Column(Float)
    country = Column(String, index=True)
    source_url = Column(String, unique=True, index=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
