#!/usr/bin/python3
"""
state - module containing the State class
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    State - the State class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new State instance
        """
        self.name = ""
        super().__init__(*args, **kwargs)
