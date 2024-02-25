import requests
from decouple import config

FRED_API_KEY = config('FRED_API_KEY')

def fetch_economic_data(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    data = response.json()
    # Process and return the data
    return data
