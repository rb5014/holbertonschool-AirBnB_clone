#!/usr/bin/python3
""" Unittest for class User
"""

import unittest
from datetime import datetime
from models.user import User


class Test_User(unittest.TestCase):
    """Test different attributes and methods of BaseModel instances
    """
    def setUp(self):
        """set up of the test instance base
        """
        self.user = User()
        self.user2 = User()
        self.d = self.user.to_dict()

    def test_attributes(self):
        """test attributes to none"""
        self.user.email = None
        self.assertEqual(self.user.email, None)
