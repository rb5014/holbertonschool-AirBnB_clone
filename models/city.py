#!/usr/bin/python3
"""
Module for the new City class
"""


from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that define Cityr's data based on BaseModel 
    """
    state_id = ""
    name = ""
