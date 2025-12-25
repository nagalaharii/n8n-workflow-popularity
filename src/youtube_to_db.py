from src.youtube_fetcher import fetch_n8n_workflow_videos
from src.crud import create_workflow_popularity, get_db


def run_youtube_etl(
    max_results=10,
    country="US",
):
    db = next(get_db())

    videos = fetch_n8n_workflow_videos(
        max_results=max_results,
        region_code=country,
    )

    inserted = 0

    for video in videos:
        try:
            create_workflow_popularity(
                db=db,
                workflow=video["workflow"],
                platform="YouTube",
                views=video["views"],
                likes=video["likes"],
                comments=video["comments"],
                country=country,
                source_url=video["source_url"],
            )
            inserted += 1
        except Exception as e:
            # Duplicate or other DB error — skip safely
            db.rollback()

    print(f"YouTube ETL finished. Inserted {inserted} records.")
