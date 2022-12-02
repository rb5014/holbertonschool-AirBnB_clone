#!/usr/bin/python3
"""
Module for the new User class
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """
    Class that define user's data based on BaseModel
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="delete", backref='user')