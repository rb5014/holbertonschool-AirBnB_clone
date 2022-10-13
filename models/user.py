#!/usr/bin/python3
"""
Module for the new User class
"""


from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that define user's data based on BaseModel 
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for User class
        """
        super().__init__()
        storage.new(self)