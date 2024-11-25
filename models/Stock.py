from sqlalchemy import Column, Integer, String, Date, Float
from database.connection import Base

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    value = Column(Float)
    date = Column(Date)