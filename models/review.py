#!/usr/bin/python3
"""
review - module containing the Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review - the Review class
    """
    place_id = ""
    user_id = ""
    text = ""
