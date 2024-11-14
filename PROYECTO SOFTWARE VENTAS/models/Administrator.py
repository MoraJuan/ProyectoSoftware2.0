from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Administrator(Base):
    __tablename__ = 'administrator'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    admin_functions = Column(String)
    user = relationship('User')