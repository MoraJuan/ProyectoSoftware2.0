from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    commercial_invoice = relationship('CommercialInvoice', back_populates='customer')

    def __repr__(self):
        return f"Cliente(nombre={self.name})"