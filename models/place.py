#!/usr/bin/python3
"""
Module for the new Place class
"""


from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """
    Class that define Place's data based on BaseModel 
    """
    city_id = City.id
    user_id = User.id
    name  = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = Amenity.id
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for Place class
        """
        super().__init__()
