#!/usr/bin/python3
"""
city - module containing the City class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City - the City class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new City instance
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
