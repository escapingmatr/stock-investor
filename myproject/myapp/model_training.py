import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def train_random_forest_model(processed_data):
    tmp = processed_data.drop(['next_day_close'], axis=1)
    latest_features = tmp.head(1)
    
    df = processed_data.dropna()  # Drop rows with NaN values to avoid issues with shifting
    
    # Prepare your features and target variable
    X = df.drop(['next_day_close'], axis=1)
    y = df['next_day_close']
    
    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and fit the model
    reg = RandomForestRegressor(n_estimators=100, random_state=42)
    reg.fit(X_train, y_train)
    
    # Make predictions
    predictions = reg.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    # Predicting the next day close price
    prediction_scaled = reg.predict(latest_features)

    # shows actual closing price
    today_close_price = processed_data['close'].head(1).values[0]

    print(f'Today closing price: {today_close_price}')
    print(f'Next day closing price: {prediction_scaled[0]}')  # Directly print the scaled prediction
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')
    
    # return the next day prediction price, mse and r2
    return prediction_scaled[0], mse, r2
