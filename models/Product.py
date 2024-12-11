from sqlalchemy import Column, Integer, String, Float
from database.connection import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    min_stock = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Producto({self.name}, stock={self.stock})"
