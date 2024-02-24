# api_integration/fred_api.py
import requests
from decouple import config

FRED_API_KEY = config('FRED_API_KEY', default='')

def fetch_economic_indicators():
    # Example: Fetching GDP data
    series_id = 'GDPC1'
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}'
    
    response = requests.get(url)
    data = response.json().get('observations', [])

    # You can process and return the data as needed
    return data
