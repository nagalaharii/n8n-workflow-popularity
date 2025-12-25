import time
from pytrends.request import TrendReq
from requests.exceptions import ReadTimeout


def fetch_google_trends_workflows(
    keywords=None, country="US", limit=5
):
    """
    Fetch Google Trends interest data safely (best-effort).
    Pipeline MUST NOT fail if Google blocks or times out.
    """

    if keywords is None:
        keywords = [
            "n8n workflow",
            "n8n automation",
            "n8n slack integration",
            "n8n whatsapp automation",
            "n8n google sheets automation",
        ]

    pytrends = TrendReq(
        hl="en-US",
        tz=360,
        timeout=(10, 25),  # ⬅ increased timeout
        retries=2,
        backoff_factor=0.3,
    )

    workflows = []

    for keyword in keywords[:limit]:
        try:
            pytrends.build_payload(
                [keyword],
                timeframe="today 3-m",
                geo=country,
            )

            interest = pytrends.interest_over_time()

            if interest.empty:
                continue

            avg_interest = int(interest[keyword].mean())

            workflows.append(
                {
                    "workflow": keyword,
                    "platform": "Google",
                    "views": avg_interest,  # proxy popularity
                    "likes": 0,
                    "comments": 0,
                    "like_to_view_ratio": 0,
                    "comment_to_view_ratio": 0,
                    "country": country,
                    "source_url": f"https://trends.google.com/trends/explore?q={keyword}",
                }
            )

            time.sleep(1)  # ⬅ avoid Google rate limiting

        except ReadTimeout:
            print(f"[WARN] Google Trends timeout for keyword: {keyword}")
            continue
        except Exception as e:
            print(f"[WARN] Google Trends error for {keyword}: {e}")
            continue

    return workflows
