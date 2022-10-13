#!/usr/bin/python3
""" Unittest for State
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State


class Test_Classes(unittest.TestCase):
    """Test different attributes and methods of state instances
    """
    def test_state(self):
        """test for state class"""
        self.assertIsInstance()