import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from .api_integration.alpha_vantage import fetch_historical_prices, fetch_technical_indicator
from .api_integration.fred_api import fetch_economic_data

def process_stock_data(symbol):
    # Example: Fetch and process historical stock prices
    historical_prices = fetch_historical_prices(symbol)
    # Convert to DataFrame (assuming the function returns a dict)
    prices_df = pd.DataFrame(historical_prices['Time Series (Daily)']).transpose()
    prices_df.columns = ['open', 'high', 'low', 'close', 'volume']
    
    # Convert columns to numeric
    for col in prices_df.columns:
        prices_df[col] = pd.to_numeric(prices_df[col], errors='coerce')

    # Feature Engineering: Create additional features if necessary
    # moving average
    prices_df['moving_average'] = prices_df['close'].rolling(window=10).mean()
    # differencing
    prices_df['close_diff'] = prices_df['close'].diff(1)

    # Normalize features
    scaler = StandardScaler()
    prices_df[['open', 'high', 'low', 'close', 'volume', 'moving_average', 'close_diff']] = scaler.fit_transform(prices_df[['open', 'high', 'low', 'close', 'volume', 'moving_average', 'close_diff']])
    
    return prices_df

def split_data(X, y):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Example usage:
# Assuming 'symbol' is defined and 'y' (target variable) is prepared
prices_df = process_stock_data('AAPL')
X = prices_df.drop(columns=['close'])  # Use features excluding target
y = prices_df['close']  # Target variable
X_train, X_test, y_train, y_test = split_data(X, y)
