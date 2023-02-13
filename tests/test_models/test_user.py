#!/usr/bin/python3
""" Unit tests for the User class """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Tests for the User class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_inheritance(self):
        """ test that User inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_str(self):
        """ test the __str__ method for User """
        my_user = User()
        s = "[{}] ({}) {}".format(my_user.__class__.__name__,
                                  my_user.id, my_user.__dict__)
        self.assertEqual(my_user.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for User """
        self.assertIs(type(User.email), str)
        self.assertEqual(User.email, "")
        self.assertIs(type(User.password), str)
        self.assertEqual(User.password, "")
        self.assertIs(type(User.first_name), str)
        self.assertEqual(User.first_name, "")
        self.assertIs(type(User.last_name), str)
        self.assertEqual(User.last_name, "")
