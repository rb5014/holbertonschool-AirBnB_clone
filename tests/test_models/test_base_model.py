#!/usr/bin/python3
""" Unittest for base_model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path


class Test_BaseModel(unittest.TestCase):
    """Test different attributes and methods of BaseModel instances
    """

    def setUp(self):
        """set up of the test instance base
        """
        self.base = BaseModel()
        self.base2 = BaseModel()
        self.d = self.base.to_dict()

    def test_attributes(self):
        """test regular attributes
        """
        self.assertNotEqual(self.base.id, self.base2.id)
        self.assertIsInstance(self.base.created_at, datetime)

    def test_save(self):
        """test method save
        """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)
        self.assertTrue(path.exists("file.json"))

    def test_to_dict(self):
        """test method to_dict
        """
        self.assertIsInstance(self.d, dict)
        self.assertTrue('__class__' in self.d)
        self.assertIsInstance(self.d['created_at'], str)
        self.assertIsInstance(self.d['updated_at'], str)

    def test__str__(self):
        """test str representation of the instance
        """
        s = f"[{self.base.__class__.__name__}] " \
            f"({self.base.id}) {self.base.__dict__}"
        self.assertEqual(self.base.__str__(), s)


class Test_FileStorage(unittest.TestCase):
    """Test different attributes and methods of FileStorage instances
    """

    def setUp(self):
        """set up of the FileStorage instance
        """
        self.storage = FileStorage()

    def test___file_path(self):
        """test of __file_path value equal to "file.json"
        """
        self.assertTrue(path.exists("file.json"))

    def test__objects(self):
        """test of __objects value equal to {}
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_all(self):
        """test of __objects value equal to storage.all()
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """test of new() adding new object to __objects
        """
        all_objs = self.storage.all().copy()
        self.base = BaseModel()
        all_objs2 = self.storage.all().copy()
        self.assertNotEqual(all_objs, all_objs2)

    def test_save(self):
        """test save() creates a file
        """
        self.storage.save()
        self.assertTrue(path.exists("file.json"))

    def test_reload(self):
        """test reload recreates all objects from "file.json"
        """
        all_objs = self.storage.all().copy()
        for key in all_objs:
            self.assertIsInstance(all_objs[key], BaseModel)
