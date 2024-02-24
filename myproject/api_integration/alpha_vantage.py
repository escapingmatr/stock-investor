# api_integration/alpha_vantage.py
import requests
from decouple import config

ALPHA_VANTAGE_API_KEY = config('ALPHA_VANTAGE_API_KEY', default='')

def fetch_stock_prices(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    
    response = requests.get(url)
    data = response.json().get('Time Series (Daily)', {})

    # You can process and return the data as needed
    return data

def fetch_financial_metrics(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    
    response = requests.get(url)
    data = response.json()

    # You can process and return the data as needed
    return data
