#!/usr/bin/python3
""" Unittest for Place
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place


class Test_Classes(unittest.TestCase):
    """Test different attributes and methods of place instances
    """
    def test_place(self):
        """test for state place"""
        self.assertIsInstance()