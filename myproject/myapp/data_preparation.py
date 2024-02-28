import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from api_integration.alpha_vantage import fetch_historical_prices, fetch_technical_indicator
from api_integration.fred_api import fetch_economic_data
import numpy as np

def calculate_rsi(data, window=14):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_stochastic_oscillator(data, window=14):
    l14 = data['low'].rolling(window=window).min()
    h14 = data['high'].rolling(window=window).max()
    k = 100 * ((data['close'] - l14) / (h14 - l14))
    return k

def calculate_williams_r(data, window=14):
    l14 = data['low'].rolling(window=window).min()
    h14 = data['high'].rolling(window=window).max()
    wr = -100 * ((h14 - data['close']) / (h14 - l14))
    return wr

def calculate_macd(data, short_window=12, long_window=26, signal=9):
    short_ema = data['close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calculate_roc(data, window=12):
    roc = data['close'].diff(window) / data['close'].shift(window) * 100
    return roc

def calculate_obv(data):
    obv = (np.sign(data['close'].diff()) * data['volume']).fillna(0).cumsum()
    return obv

def process_stock_data(symbol):
    historical_prices = fetch_historical_prices(symbol)
    prices_df = pd.DataFrame(historical_prices['Time Series (Daily)']).transpose()
    prices_df.columns = ['open', 'high', 'low', 'close', 'volume']
    
    for col in prices_df.columns:
        prices_df[col] = pd.to_numeric(prices_df[col], errors='coerce')

    prices_df['rsi'] = calculate_rsi(prices_df)
    prices_df['stoch_osc'] = calculate_stochastic_oscillator(prices_df)
    prices_df['williams_r'] = calculate_williams_r(prices_df)
    macd, signal_line = calculate_macd(prices_df)
    prices_df['macd'] = macd
    prices_df['macd_signal'] = signal_line
    prices_df['roc'] = calculate_roc(prices_df)
    prices_df['obv'] = calculate_obv(prices_df)
    prices_df['next_day_close'] = prices_df['close'].shift(-1)

    # scaler = StandardScaler()
    # feature_columns = ['open', 'high', 'low', 'next_day_close', 'volume', 'rsi', 'stoch_osc', 'williams_r', 'macd', 'macd_signal', 'roc', 'obv']
    # prices_df[feature_columns] = scaler.fit_transform(prices_df[feature_columns])
    
    return prices_df

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
