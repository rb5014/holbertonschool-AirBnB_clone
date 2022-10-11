#!/usr/bin/python3
""" Unittest for file_storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


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
        FileStorage.__file_path = None
        b = BaseModel()
        b.save()
        self.storage.reload()
        with self.assertRaises(Exception):
            self.assertTrue(os.path.exists(FileStorage.__file_path))
        FileStorage.__file_path = "file.json"
        b.save()
        self.storage.reload()
        self.assertTrue(os.path.exists(FileStorage.__file_path))
        
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
        base = BaseModel()
        all_objs2 = self.storage.all().copy()
        self.assertNotEqual(all_objs, all_objs2)

    def test_save(self):
        """test save() creates a file
        """
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test reload recreates all objects from "file.json"
        """
        all_objs = self.storage.all().copy()
        for key in all_objs:
            self.assertIsInstance(all_objs[key], BaseModel)

    if __name__ == "__main__":
        unittest.main()
