from django.core.management.base import BaseCommand
from api_integration.alpha_vantage import fetch_historical_prices, fetch_technical_indicator
from api_integration.fred_api import fetch_economic_data

class Command(BaseCommand):
    help = 'Fetch stock data and economic indicators.'

    def handle(self, *args, **options):
        symbol = 'AAPL'  # Example symbol
        # Fetch historical stock prices
        stock_data = fetch_historical_prices(symbol)
        # Fetch a technical indicator, e.g., RSI
        rsi_data = fetch_technical_indicator(symbol, 'RSI')
        # Fetch economic data from FRED, e.g., GDP
        gdp_data = fetch_economic_data('GDPC1')
        
        # Here, add your logic to process and save this data
        # This could involve parsing the responses and storing them in your database
        
        self.stdout.write(self.style.SUCCESS('Successfully fetched data.'))
