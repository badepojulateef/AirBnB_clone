#!/usr/bin/python3
"""
place - module containing the Place class
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Place - the Place class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new Place instance
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0
        self.longitude = 0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
