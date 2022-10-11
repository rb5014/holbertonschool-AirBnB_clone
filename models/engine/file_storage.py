#!/usr/bin/python3
"""
Module containing the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """
    Serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    # (ex: to store a BaseModel object with id=12121212,
    # the key will be BaseModel.12121212)
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + "." +
                              str(obj.id)] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w+', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to
        __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
