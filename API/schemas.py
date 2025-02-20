from pydantic import BaseModel
from typing import List

class ModelData(BaseModel):
    input_data: str
    output_data: int

class ModelData(ModelData):
    id: int
    class Config:
        orm_mode = True


class PredictionInput(BaseModel):
    data: List[int]  # Массив целых чисел 

class PredictionOutput(BaseModel):
    prediction: int  # Целое число предсказания