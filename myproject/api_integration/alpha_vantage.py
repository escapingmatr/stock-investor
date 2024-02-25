import requests
from decouple import config

ALPHA_VANTAGE_API_KEY = config('ALPHA_VANTAGE_API_KEY')

def fetch_historical_prices(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=full"
    response = requests.get(url)
    data = response.json()
    # Process and return the data
    return data

def fetch_technical_indicator(symbol, indicator):
    url = f"https://www.alphavantage.co/query?function={indicator}&symbol={symbol}&interval=daily&time_period=10&series_type=close&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    # Process and return the data
    return data
