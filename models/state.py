#!/usr/bin/python3
"""
Module for the new State class
"""


from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that define State's data based on BaseModel 
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for State class
        """

        super().__init__()