#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    BaseModel class - common attributes/methods for all other classes
    """
    def __init__(self, *args, **kwargs):
        """ initialization of a BaseModel instance """
        if len(kwargs) > 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ get the string representation of an instance """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ update the attribute `update_at` with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        return a dictionary containing all attributes of the instance
        and their values
        """
        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = dct["created_at"].isoformat()
        dct["updated_at"] = dct["updated_at"].isoformat()
        return dct
