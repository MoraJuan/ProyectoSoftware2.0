from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    employee_functions = Column(String)
    user = relationship('User')