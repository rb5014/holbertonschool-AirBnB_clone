#!/usr/bin/python3
""" Unittest for class User
"""

import unittest
from datetime import datetime
from models.user import User
from unittest import mock


class Test_User(unittest.TestCase):
    """Test different attributes and methods of User instances
    """

    def setUp(self):
        """set up of the test instance user
        """
        self.user = User()
        self.user2 = User()
        self.d = self.user.to_dict()

    def test_attributes(self):
        """test regular attributes
        """
        self.assertNotEqual(self.user.id, self.user2.id)
        self.assertIsInstance(self.user.created_at, datetime)

    @mock.patch('models.storage.save')
    def test_save(self, mock_save):
        """test method save
        """
        old_created_at = self.user.created_at
        old_updated_at = self.user.updated_at
        self.user.save()
        new_created_at = self.user.created_at
        new_updated_at = self.user.updated_at
        self.assertEqual(old_created_at, new_created_at)
        self.assertNotEqual(new_created_at, new_updated_at)
        self.assertNotEqual(old_updated_at, new_updated_at)
        mock_save.assert_called_once()

    def test_to_dict(self):
        """test method to_dict
        """
        self.assertIsInstance(self.d, dict)
        self.assertTrue('__class__' in self.d)
        self.assertIsInstance(self.d['created_at'], str)
        self.assertIsInstance(self.d['updated_at'], str)
        self.assertFalse('email' in self.d)
        self.assertFalse('password' in self.d)
        self.assertFalse('first_name' in self.d)
        self.assertFalse('last_name' in self.d)
        self.user.email = None
        self.user.password = None
        self.user.first_name = None
        self.user.last_name = None
        self.d = self.user.to_dict()
        self.assertFalse(self.d['email'])
        self.assertFalse(self.d['password'])
        self.assertFalse(self.d['first_name'])
        self.assertFalse(self.d['last_name'])

    def test__str__(self):
        """test str representation of the instance
        """
        s = f"[{self.user.__class__.__name__}] " \
            f"({self.user.id}) {self.user.__dict__}"
        self.assertEqual(self.user.__str__(), s)

    if __name__ == "__main__":
        unittest.main()
