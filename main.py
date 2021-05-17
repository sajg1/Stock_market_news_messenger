import requests
import datetime
import os

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

# using environment variable to store API key
API_KEY = os.environ.get("STOCK_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": API_KEY
}
# Fetch daily stock information for Tesla
stock_response = requests.get(url=STOCK_URL, params=stock_parameters)

stock_data = stock_response.json()

# Created a list of all daily closing prices for this stock
daily_stock_prices = [value['4. close'] for (key, value) in stock_data["Time Series (Daily)"].items()]

# Isolate the  last to days closing prices and find the price diff and the percentage diff
yesterdays_closing_price = daily_stock_prices[0]
day_before_yesterday_closing_price = daily_stock_prices[1]

closing_price_diff = round(float(yesterdays_closing_price) - float(day_before_yesterday_closing_price), 2)
percentage_price_diff = round((closing_price_diff / float(day_before_yesterday_closing_price)) * 100, 2)

if percentage_price_diff > 3:

    d1 = datetime.datetime.now()
    new_format = "%Y-%m-%d"
    CURRENT_DATE = d1.strftime(new_format)

    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    news_parameters = {
        "q": "tesla",
        "from": CURRENT_DATE,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_data = news_response.json()
    news_articles = news_data['articles']
    top_3_articles = news_articles[:3]
    # isolated just the headlines and descriptions of the current top 3 articles regarding Tesla
    top_3_articles_headlines_and_stories = [{x['title']: x['description']} for x in top_3_articles]
    print(top_3_articles_headlines_and_stories)
