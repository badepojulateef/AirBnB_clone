#!/usr/bin/python3
"""
amenity - module containing the Amenity class
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity - the Amenity class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new Amenity instance
        """
        self.name = ""
        super().__init__(*args, **kwargs)
