#!/usr/bin/python3
""" Unit tests for the State class """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Tests for the State class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_inheritance(self):
        """ test that State inherits from BaseModel """
        self.assertTrue(issubclass(State, BaseModel))

    def test_str(self):
        """ test the __str__ method for State """
        my_state = State()
        s = "[{}] ({}) {}".format(my_state.__class__.__name__,
                                  my_state.id, my_state.__dict__)
        self.assertEqual(my_state.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for State """
        self.assertIs(type(State.name), str)
        self.assertEqual(State.name, "")
