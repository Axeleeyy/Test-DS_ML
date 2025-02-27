from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class UserRequest(Base):
    __tablename__ = 'user_requests'

    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    request = Column(String)
    result = Column(Integer)

    user = relationship('User', back_populates='requests')

User.requests = relationship('UserRequest', order_by=UserRequest.id, back_populates='user')

class ModelData(Base):
    __tablename__ = "model_data"
    id = Column(Integer, primary_key=True, index=True)
    Elevation = Column(Integer) 
    Aspect = Column(Integer)
    Slope = Column(Integer)
    Horizontal_Distance_To_Hydrology = Column(Integer)
    Vertical_Distance_To_Hydrology = Column(Integer)
    Horizontal_Distance_To_Roadways = Column(Integer)
    Hillshade_9am = Column(Integer)
    Hillshade_Noon = Column(Integer)
    Hillshade_3pm = Column(Integer)
    Horizontal_Distance_To_Fire_Points = Column(Integer)
    Wilderness_Area = Column(Integer)
    Soil_Type = Column(Integer)
    Cover_Type = Column(Integer)

