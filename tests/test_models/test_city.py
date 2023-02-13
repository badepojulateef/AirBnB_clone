#!/usr/bin/python3
""" Unit tests for the City class """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Tests for the City class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_inheritance(self):
        """ test that City inherits from BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_str(self):
        """ test the __str__ method for City """
        my_city = City()
        s = "[{}] ({}) {}".format(my_city.__class__.__name__,
                                  my_city.id, my_city.__dict__)
        self.assertEqual(my_city.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for City """
        self.assertIs(type(City.state_id), str)
        self.assertEqual(City.state_id, "")
        self.assertIs(type(City.name), str)
        self.assertEqual(City.name, "")
