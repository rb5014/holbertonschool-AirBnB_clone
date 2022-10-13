#!/usr/bin/python3
""" Unittest for State, City, Amenity, Place and Review
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City

class Test_Classes(unittest.TestCase):
    """Test different attributes and methods of city instances
    """
    def test_state(self):
        """test for city class"""
        self.assertIsInstance()