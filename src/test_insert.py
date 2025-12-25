from src.crud import create_workflow_popularity, get_db

db = next(get_db())

record = create_workflow_popularity(
    db=db,
    workflow="Google Sheets → Slack Automation",
    platform="YouTube",
    views=12500,
    likes=630,
    comments=88,
    country="US",
    source_url="https://youtube.com/example-video"
)

print("Inserted:", record)
