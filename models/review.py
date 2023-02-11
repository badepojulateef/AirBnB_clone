#!/usr/bin/python3
"""
review - module containing the Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review - the Review class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new Review instance
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
