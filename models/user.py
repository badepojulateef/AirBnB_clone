#!/usr/bin/python3
"""
user - module containing the User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User - the User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
