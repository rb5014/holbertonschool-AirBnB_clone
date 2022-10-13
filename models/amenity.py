#!/usr/bin/python3
"""
Module for the new Amenity class
"""


from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class that define Amenity's data based on BaseModel 
    """
    name = ""
