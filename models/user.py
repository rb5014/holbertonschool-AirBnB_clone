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

    def __init__(self, *args, **kwargs):
        """
        Constructor for User class
        """

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        storage.new(self)
