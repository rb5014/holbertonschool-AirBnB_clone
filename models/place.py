#!/usr/bin/python3
"""
Module for the new Place class
"""


from models import storage
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class that define Place's data based on BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
