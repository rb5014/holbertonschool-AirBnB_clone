#!/usr/bin/python3
"""
Module for the new Review class
"""


from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that define Review's data based on BaseModel 
    """
    place_id = ""
    user_id = ""
    text = ""
