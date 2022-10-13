#!/usr/bin/python3
"""
Module for the new Review class
"""


from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.user import User



class Review(BaseModel):
    """
    Class that define Review's data based on BaseModel 
    """
    place_id = Place.id
    user_id = User.id
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for Review class
        """
        super().__init__()
