import requests
import os

STOCK_URL = "https://www.alphavantage.co/query"

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
yesterdays_closing_price = daily_stock_prices[0]
print(yesterdays_closing_price)

