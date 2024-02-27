from django.core.management.base import BaseCommand
# Import your data preparation and model training functions
from myapp.data_preparation import process_stock_data
from myapp.model_training import train_random_forest_model  # Assume you have this

class Command(BaseCommand):
    help = 'Fetches data, prepares it, and trains a Random Forest model.'

    def add_arguments(self, parser):
        # Optional: Add arguments to specify stock symbols or other parameters
        parser.add_argument('symbol', type=str, help='Stock symbol for which to train the model')

    def handle(self, *args, **options):
        symbol = options['symbol']
        self.stdout.write(self.style.SUCCESS(f'Starting data preparation for {symbol}...'))
        
        # Step 1: Data Preparation
        processed_data = process_stock_data(symbol)
        self.stdout.write(self.style.SUCCESS(f'Data preparation completed for {symbol}.'))

        # Step 2: Model Training
        # Assuming `train_random_forest_model` takes processed data and returns model performance
        performance_metrics = train_random_forest_model(processed_data)
        
        # Output the results
        self.stdout.write(self.style.SUCCESS(f'Model trained successfully. Performance: {performance_metrics}'))
