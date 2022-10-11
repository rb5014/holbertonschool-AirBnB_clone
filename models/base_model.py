#!/usr/bin/python3
''' Base Module for python interpreter'''


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Parent class to store data'''

    def __init__(self, *args, **kwargs):
        '''BaseModel Constructor'''

        if kwargs:
            self.update(*args, **kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''Method to change print output of the instance'''

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
        Public method to update public instance and store the
        change in the public instance attribute <updated_at>
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Used to return a dict of all attribute of the instance'''
        # Create the dict
        dictInst = self.__dict__.copy()
        # Add a key '__class__' with value: the class name of the object
        dictInst['__class__'] = self.__class__.__name__
        dictInst['created_at'] = datetime.isoformat(dictInst['created_at'])
        dictInst['updated_at'] = datetime.isoformat(dictInst['updated_at'])
        return dictInst

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute(keys) in kwargs
        """
        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.fromisoformat(value))
            elif key != '__class__':
                setattr(self, key, value)
