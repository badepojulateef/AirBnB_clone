#!/usr/bin/env python3
""" A module that implements the BaseModel class """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A base or super class from which all other classes
    inherits the common attributes/methods
    """
    def __init__(self):
        """ Initializes the instance attributes """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
