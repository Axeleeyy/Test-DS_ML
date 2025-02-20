from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import ModelData
from schemas import ModelData as ModelDataSchema
from schemas import PredictionInput, PredictionOutput
from auth import get_current_user
from typing import List
from fastapi import FastAPI
import models
import joblib
from pandas import DataFrame

# Загрузка модели
model = joblib.load('../data/model.pkl')

# Создание базы данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def predict(data: List[int]) -> int:
    #логика для предсказания результата
    dfData = DataFrame([data], columns=['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology', 
 'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways', 
 'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm', 
 'Horizontal_Distance_To_Fire_Points', 'Wilderness_Area', 'Soil_Type']) # len = 12
    prediction = model.predict(dfData)

    return prediction   #результат предсказания


@app.post("/predict/", response_model=PredictionOutput)
async def make_prediction(input_data: PredictionInput):
    if len(input_data.data) != 12:
        raise HTTPException(status_code=400, detail="Input data must be an array of length 12.")
    
    prediction = predict(input_data.data)
    return PredictionOutput(prediction=prediction)

