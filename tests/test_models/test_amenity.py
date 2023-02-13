#!/usr/bin/python3
""" Unit tests for the Amenity class """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests for the Amenity class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_inheritance(self):
        """ test that Amenity inherits from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_str(self):
        """ test the __str__ method for Amenity """
        my_amenity = Amenity()
        s = "[{}] ({}) {}".format(my_amenity.__class__.__name__,
                                  my_amenity.id, my_amenity.__dict__)
        self.assertEqual(my_amenity.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for Amenity """
        self.assertIs(type(Amenity.name), str)
        self.assertEqual(Amenity.name, "")
