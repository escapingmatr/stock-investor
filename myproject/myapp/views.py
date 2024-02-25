from django.shortcuts import render
from django.http import HttpResponse
# Import your data fetching functions
from .api_integration.alpha_vantage import fetch_historical_prices, fetch_technical_indicator
from .api_integration.fred_api import fetch_economic_data

def fetch_data_view(request):
    # Similar to the command, fetch and process data here
    symbol = "AAPL"
    prices = fetch_historical_prices(symbol)
    # Process and respond
    return HttpResponse("Data fetched successfully.")
