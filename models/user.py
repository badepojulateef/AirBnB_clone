#!/usr/bin/python3
"""
user - module containing the User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User - the User class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new User instance
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
