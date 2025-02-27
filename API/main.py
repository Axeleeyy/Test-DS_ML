from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from schemas import PredictionInput, PredictionOutput, InputData, OutputData
from typing import List
import models
import joblib
from pandas import DataFrame
from models import Base, ModelData
from auth import router as auth_router  
from auth import oauth2_scheme



app = FastAPI(title='Predict Model')

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Подключение маршрутов авторизации
app.include_router(auth_router)

# Загрузка модели
model = joblib.load('../data/model.pkl')

# Создание базы данных
models.Base.metadata.create_all(bind=engine)


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

def get_data(db: Session, record_id: int):
    """
    getting modeldata
    """

    return db.query(ModelData).filter(ModelData.id == record_id).first()

def get_df(data: dict) -> dict:
    """
    compress input data
    """
    dfData = DataFrame(data) 
    a = []
    for i in range(len(dfData)):
        for x in range(1, 5):
            if data["Wilderness_Area" + str(x)][i]:
                a.append(x)

    for x in range(1, 5):
        dfData = dfData.drop("Wilderness_Area" + str(x), axis=1)
    dfData['Wilderness_Area'] = a

    a.clear()
    for i in range(len(dfData)):
        for x in range(1, 41):
            if data["Soil_Type" + str(x)][i]:
                a.append(x)
    for x in range(1, 41):
        dfData = dfData.drop("Soil_Type" + str(x), axis=1)
    dfData['Soil_Type'] = a

    return dfData

def predict_data(data: dict) -> int:
    """
    prediction value by model
    """
    if len(data) > 14:
        dfData = get_df(data)
    else:
        dfData = data
    
    prediction = model.predict(dfData)

    return int(prediction)   #результат предсказания

def save_data(db: Session, data: dict) -> int:
    """
    saving a dict in db
    """
    record = ModelData(
        Elevation = int(data["Elevation"][0]),
        Aspect = int(data["Aspect"][0]),
        Slope = int(data["Slope"][0]),
        Horizontal_Distance_To_Hydrology = int(data["Horizontal_Distance_To_Hydrology"][0]),
        Vertical_Distance_To_Hydrology = int(data["Vertical_Distance_To_Hydrology"][0]),
        Horizontal_Distance_To_Roadways = int(data["Horizontal_Distance_To_Roadways"][0]),
        Hillshade_9am = int(data["Hillshade_9am"][0]),
        Hillshade_Noon = int(data["Hillshade_Noon"][0]),
        Hillshade_3pm = int(data["Hillshade_3pm"][0]),
        Horizontal_Distance_To_Fire_Points = int(data["Horizontal_Distance_To_Fire_Points"][0]),
        Wilderness_Area = int(data["Wilderness_Area"][0]),
        Soil_Type = int(data["Soil_Type"][0]),
        Cover_Type = int(data["Cover_Type"][0])
    )

   
    db.add(record)
   
    db.commit()
    db.refresh(record)
    
    return record.id


@app.get("/predict", response_model=dict)
def predict(
    Elevation: int = Query(...),
    Aspect: int = Query(...),
    Slope: int = Query(...),
    Horizontal_Distance_To_Hydrology: int = Query(...),
    Vertical_Distance_To_Hydrology: int = Query(...),
    Horizontal_Distance_To_Roadways: int = Query(...),
    Hillshade_9am: int = Query(...),
    Hillshade_Noon: int = Query(...),
    Hillshade_3pm: int = Query(...),
    Horizontal_Distance_To_Fire_Points: int = Query(...),
    Wilderness_Area1: int = Query(...),
    Wilderness_Area2: int = Query(...),
    Wilderness_Area3: int = Query(...),
    Wilderness_Area4: int = Query(...),
    Soil_Type1: int = Query(...),
    Soil_Type2: int = Query(...),
    Soil_Type3: int = Query(...),
    Soil_Type4: int = Query(...),
    Soil_Type5: int = Query(...),
    Soil_Type6: int = Query(...),
    Soil_Type7: int = Query(...),
    Soil_Type8: int = Query(...),
    Soil_Type9: int = Query(...),
    Soil_Type10: int = Query(...),
    Soil_Type11: int = Query(...),
    Soil_Type12: int = Query(...),
    Soil_Type13: int = Query(...),
    Soil_Type14: int = Query(...),
    Soil_Type15: int = Query(...),
    Soil_Type16: int = Query(...),
    Soil_Type17: int = Query(...),
    Soil_Type18: int = Query(...),
    Soil_Type19: int = Query(...),
    Soil_Type20: int = Query(...),
    Soil_Type21: int = Query(...),
    Soil_Type22: int = Query(...),
    Soil_Type23: int = Query(...),
    Soil_Type24: int = Query(...),
    Soil_Type25: int = Query(...),
    Soil_Type26: int = Query(...),
    Soil_Type27: int = Query(...),
    Soil_Type28: int = Query(...),
    Soil_Type29: int = Query(...),
    Soil_Type30: int = Query(...),
    Soil_Type31: int = Query(...),
    Soil_Type32: int = Query(...),
    Soil_Type33: int = Query(...),
    Soil_Type34: int = Query(...),
    Soil_Type35: int = Query(...),
    Soil_Type36: int = Query(...),
    Soil_Type37: int = Query(...),
    Soil_Type38: int = Query(...),
    Soil_Type39: int = Query(...),
    Soil_Type40: int = Query(...),
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> int:
    # Создаем словарь из параметров
    data = {
        "Elevation": [Elevation],
        "Aspect": [Aspect],
        "Slope": [Slope],
        "Horizontal_Distance_To_Hydrology": [Horizontal_Distance_To_Hydrology],
        "Vertical_Distance_To_Hydrology": [Vertical_Distance_To_Hydrology],
        "Horizontal_Distance_To_Roadways": [Horizontal_Distance_To_Roadways],
        "Hillshade_9am": [Hillshade_9am],
        "Hillshade_Noon": [Hillshade_Noon],
        "Hillshade_3pm": [Hillshade_3pm],
        "Horizontal_Distance_To_Fire_Points": [Horizontal_Distance_To_Fire_Points],
        "Wilderness_Area1": [Wilderness_Area1],
        "Wilderness_Area2": [Wilderness_Area2],
        "Wilderness_Area3": [Wilderness_Area3],
        "Wilderness_Area4": [Wilderness_Area4],
        "Soil_Type1": [Soil_Type1],
        "Soil_Type2": [Soil_Type2],
        "Soil_Type3": [Soil_Type3],
        "Soil_Type4": [Soil_Type4],
        "Soil_Type5": [Soil_Type5],
        "Soil_Type6": [Soil_Type6],
        "Soil_Type7": [Soil_Type7],
        "Soil_Type8": [Soil_Type8],
        "Soil_Type9": [Soil_Type9],
        "Soil_Type10": [Soil_Type10],
        "Soil_Type11": [Soil_Type11],
        "Soil_Type12": [Soil_Type12],
        "Soil_Type13": [Soil_Type13],
        "Soil_Type14": [Soil_Type14],
        "Soil_Type15": [Soil_Type15],
        "Soil_Type16": [Soil_Type16],
        "Soil_Type17": [Soil_Type17],
        "Soil_Type18": [Soil_Type18],
        "Soil_Type19": [Soil_Type19],
        "Soil_Type20": [Soil_Type20],
        "Soil_Type21": [Soil_Type21],
        "Soil_Type22": [Soil_Type22],
        "Soil_Type23": [Soil_Type23],
        "Soil_Type24": [Soil_Type24],
        "Soil_Type25": [Soil_Type25],
        "Soil_Type26": [Soil_Type26],
        "Soil_Type27": [Soil_Type27],
        "Soil_Type28": [Soil_Type28],
        "Soil_Type29": [Soil_Type29],
        "Soil_Type30": [Soil_Type30],
        "Soil_Type31": [Soil_Type31],
        "Soil_Type32": [Soil_Type32],
        "Soil_Type33": [Soil_Type33],
        "Soil_Type34": [Soil_Type34],
        "Soil_Type35": [Soil_Type35],
        "Soil_Type36": [Soil_Type36],
        "Soil_Type37": [Soil_Type37],
        "Soil_Type38": [Soil_Type38],
        "Soil_Type39": [Soil_Type39],
        "Soil_Type40": [Soil_Type40]
    }
    
    data = get_df(data)
    result = predict_data(data)

    data['Cover_Type'] = [result]

    id = save_data(db, data)


    return {"id": id, "result": result}

def get_modeldata(record: ModelData):
    """
    getting a dictionary with data
    """
    data = {
        "id": record.id,
        "Elevation": record.Elevation,
        "Aspect": record.Aspect,
        "Slope": record.Slope,
        "Horizontal_Distance_To_Hydrology": record.Horizontal_Distance_To_Hydrology,
        "Vertical_Distance_To_Hydrology": record.Vertical_Distance_To_Hydrology,
        "Horizontal_Distance_To_Roadways": record.Horizontal_Distance_To_Roadways,
        "Hillshade_9am": record.Hillshade_9am,
        "Hillshade_Noon": record.Hillshade_Noon,
        "Hillshade_3pm": record.Hillshade_3pm,
        "Horizontal_Distance_To_Fire_Points": record.Horizontal_Distance_To_Fire_Points,
        "Wilderness_Area": record.Wilderness_Area,
        "Soil_Type": record.Soil_Type,
        "Cover_Type": record.Cover_Type
    }
    return data



@app.get("/data/{record_id}", response_model=dict)
def read_data_by_id(record_id: int, db: Session = Depends(get_db)):
    record = get_data(db, record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")

    data = get_modeldata(record)

    return data

def get_all_record_ids(db: Session):
    return db.query(ModelData.id).all()


@app.get("/data", response_model=list)
def read_data(db: Session = Depends(get_db)):
    ids = get_all_record_ids(db)

    return [get_modeldata(get_data(db, x[0])) for x in ids]


def delete_data(db: Session, record_id: int):
    record = get_data(db, record_id)
    if record:
        db.delete(record)
        db.commit()
        return True
    return False

@app.delete("/data/{record_id}", response_model=dict)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    success = delete_data(db, record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"detail": "Record deleted successfully"}