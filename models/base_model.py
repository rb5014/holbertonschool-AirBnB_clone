#!/usr/bin/python3
''' Base Module for python interpreter'''


import uuid
from datetime import datetime


class BaseModel:
    '''Parent class to store data'''

    def __init__(self):
        '''BaseModel Constructor'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.isoformat(datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        '''Method to change print output of the instance'''

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_save(self):
        '''
        Public method to update public instance and store the
        change in the public instance attribute <updated_at>
        '''

        self.updated_at = datetime.isoformat(datetime.now())

    def to_dict(self):
        '''Used to return a dict of all attribute of the instance'''
        # Create the dict
        dictInst = self.__dict__
        # Add a key '__class__' with value: the class name of the object
        dictInst['__class__'] = self.__class__.__name__
        return dictInst
