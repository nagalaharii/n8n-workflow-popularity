# Fetch Google Trends interest for n8n workflow keywords
# Countries: US and IN
# Calculate 30-day and 60-day trend changes
import os
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
def fetch_google_trends_data(keyword, timeframe='today 3-m', geo='US'):
    pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)
    interest_over_time = pytrends.interest_over_time()
    if interest_over_time.empty:
        return {}
    latest_value = interest_over_time[keyword].iloc[-1]
    past_30_days_value = interest_over_time[keyword].iloc[-30]
    past_60_days_value = interest_over_time[keyword].iloc[-60]
    change_30_days = ((latest_value - past_30_days_value) / past_30_days_value * 100) if past_30_days_value != 0 else 0
    change_60_days = ((latest_value - past_60_days_value) / past_60_days_value * 100) if past_60_days_value != 0 else 0
    return {
        "keyword": keyword,
        "latest_interest": latest_value,
        "change_30_days": change_30_days,
        "change_60_days": change_60_days,
        "geo": geo,
    }
# Example usage:
if __name__ == "__main__":
    keyword = "n8n workflow"
    us_trends = fetch_google_trends_data(keyword, geo='US')
    in_trends = fetch_google_trends_data(keyword, geo='IN')
    print("US Trends:", us_trends)
    print("IN Trends:", in_trends)
    