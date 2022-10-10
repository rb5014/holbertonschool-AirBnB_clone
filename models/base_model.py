#!/usr/bin/python3
''' Base Module for python interpreter'''


import uuid
import datetime


class BaseModel:
    '''Parent class to store data'''

    def __init__(self):
        '''BaseModel Constructor'''

        self.id = uuid.uuid4()
        self.created_at = isoformat(datetime.datetime)
        self.updated_at = None

    def __str__(self):
        '''Method to change print output of the instance'''

        return ("[{}] ({}) {}".format(self.__name__, self.id, self.__dict__))

    def to_save(self):
        '''
        Public method to update public instance and store the
        change in the public instance attribute <updated_at>
        '''

        self.updated_at = isoformat(datetime.datetime)

    def to_dict(self):
        '''Used to return a dict of all attribute of the instance'''


