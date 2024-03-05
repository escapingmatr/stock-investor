##################################################################################
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Now you can import your Django models and use them as usual
from myapp.models import MyModel
##################################################################################
from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/predict/")
async def predict(stock_code: str):
    # Placeholder for the prediction logic
    prediction = "123.45"  # Replace with actual model prediction logic
    return {"stock_code": stock_code, "prediction": prediction}
