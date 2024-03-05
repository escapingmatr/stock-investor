import os
import django
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.model_training import train_random_forest_model

app = FastAPI()

@app.post("/predict/")
async def predict(stock_code: str):
    # Assuming `train_random_forest_model` returns a prediction
    prediction, mse, r2 = train_random_forest_model(stock_code)
    return {"stock_code": stock_code, "prediction": prediction, "mse": mse, "r2": r2}
