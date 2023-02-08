#!/usr/bin/env python3
""" A module that implements the BaseModel class """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A base or super class from which all other classes
    inherits the common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """ Initializes the instance attributes """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """ Returns a new and customized string represented """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
