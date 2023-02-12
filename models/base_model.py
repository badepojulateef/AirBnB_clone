#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class - common attributes/methods for all other classes
    """
    def __init__(self, *args, **kwargs):
        """ Initializes the instance attributes """
        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """ Returns a new and customized string represented """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the 'updated_at' with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/val pairs """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for key, val in my_dict.items():
            if key in ("created_at", "updated_at"):
                my_dict[key] = my_dict[key].isoformat()
        return my_dict
