#!/usr/bin/python3
""" Unit tests for the Place class """
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Tests for the Place class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_inheritance(self):
        """ test that Place inherits from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_str(self):
        """ test the __str__ method for Place """
        my_place = Place()
        s = "[{}] ({}) {}".format(my_place.__class__.__name__,
                                  my_place.id, my_place.__dict__)
        self.assertEqual(my_place.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for Place """
        self.assertIs(type(Place.city_id), str)
        self.assertEqual(Place.city_id, "")
        self.assertIs(type(Place.name), str)
        self.assertEqual(Place.name, "")
        self.assertIs(type(Place.description), str)
        self.assertEqual(Place.description, "")
        self.assertIs(type(Place.number_rooms), int)
        self.assertEqual(Place.number_rooms, 0)
        self.assertIs(type(Place.number_bathrooms), int)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertIs(type(Place.max_guest), int)
        self.assertEqual(Place.max_guest, 0)
        self.assertIs(type(Place.price_by_night), int)
        self.assertEqual(Place.price_by_night, 0)
        self.assertIs(type(Place.latitude), float)
        self.assertEqual(Place.latitude, 0.0)
        self.assertIs(type(Place.longitude), float)
        self.assertEqual(Place.longitude, 0.0)
        self.assertIs(type(Place.amenity_ids), list)
        self.assertEqual(Place.amenity_ids, [])
