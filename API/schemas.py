from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    

class UserRequestCreate(BaseModel):
    request_data: str


class UserRequestResponse(BaseModel):
    id: int
    user_id: int 
    request_data:str
    result_data: int
    

class InputData(BaseModel):
    Id: int
    Elevation: int
    Aspect: int
    Slope: int
    Horizontal_Distance_To_Hydrology: int
    Vertical_Distance_To_Hydrology: int
    Horizontal_Distance_To_Roadways: int
    Hillshade_9am: int
    Hillshade_Noon: int
    Hillshade_3pm: int
    Horizontal_Distance_To_Fire_Points: int
    Wilderness_Area1: int
    Wilderness_Area2: int
    Wilderness_Area3: int
    Wilderness_Area4: int
    Soil_Type1: int
    Soil_Type2: int
    Soil_Type3: int
    Soil_Type4: int
    Soil_Type5: int
    Soil_Type6: int
    Soil_Type7: int
    Soil_Type8: int
    Soil_Type9: int
    Soil_Type10: int
    Soil_Type11: int
    Soil_Type12: int
    Soil_Type13: int
    Soil_Type14: int
    Soil_Type15: int
    Soil_Type16: int
    Soil_Type17: int
    Soil_Type18: int
    Soil_Type19: int
    Soil_Type20: int
    Soil_Type21: int
    Soil_Type22: int
    Soil_Type23: int
    Soil_Type24: int
    Soil_Type25: int
    Soil_Type26: int
    Soil_Type27: int
    Soil_Type28: int
    Soil_Type29: int
    Soil_Type30: int
    Soil_Type31: int
    Soil_Type32: int
    Soil_Type33: int
    Soil_Type34: int
    Soil_Type35: int
    Soil_Type36: int
    Soil_Type37: int
    Soil_Type38: int
    Soil_Type39: int
    Soil_Type40: int

class OutputData(BaseModel):
    Cover_Type: int

class PredictionInput(BaseModel):
    data: List[int]  # Массив целых чисел 

class PredictionOutput(BaseModel):
    prediction: int  # Целое число предсказания