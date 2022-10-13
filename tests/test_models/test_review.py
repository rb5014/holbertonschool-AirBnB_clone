#!/usr/bin/python3
""" Unittest for Review
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.review import Review



class Test_Classes(unittest.TestCase):
    """Test different attributes and methods of review instances
    """
    def test_state(self):
        """test for review class"""
        self.assertIsInstance()