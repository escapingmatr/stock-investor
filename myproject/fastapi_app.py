import os
import django
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.model_training import train_random_forest_model
from myapp.data_preparation import process_stock_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # The Vue.js app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    stock_code: str

class PredictionResponse(BaseModel):
    stock_code: str
    prediction: float
    mse: float
    r2: float

@app.post("/predict/", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Fetch and prepare data for the given stock code
    prepared_data = process_stock_data(request.stock_code)  # Assuming this now returns a DataFrame and a scaler
    if prepared_data is None:
        return {"error": "Failed to fetch or prepare data for the given stock code."}
    
    # Ensure that train_random_forest_model is updated to accept a DataFrame and return prediction, mse, and r2
    prediction, mse, r2 = train_random_forest_model(prepared_data)  # Pass the DataFrame to your model training function
    return PredictionResponse(stock_code=request.stock_code, prediction=prediction, mse=mse, r2=r2)
