from sqlalchemy import Column, Integer, String, Float
from database import Base

class ModelData(Base):
    __tablename__ = 'model_data'
    
    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(String, index=True)
    output_data = Column(Integer)