#!/usr/bin/python3
""" Unittest for base_model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test different attributes and methods of BaseModel instances
    """

    def setUp(self):
        """set up of he test instance base
        """
        self.base = BaseModel()
        self.d = self.base.to_dict()

    def test_save(self):
        """test method save
        """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """test method to_dict
        """
        self.assertIsInstance(self.d, dict)
        self.assertTrue('__class__' in self.d)
        self.assertIsInstance(self.d['created_at'], str)
        self.assertIsInstance(self.d['updated_at'], str)
