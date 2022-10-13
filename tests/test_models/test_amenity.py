#!/usr/bin/python3
""" Unittest for Amenity
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Classes(unittest.TestCase):
    """Test different attributes and methods of amenity instances
    """
    def test_state(self):
        """test for amenity class"""
        self.assertIsInstance()