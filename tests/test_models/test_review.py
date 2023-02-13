#!/usr/bin/python3
""" Unit tests for the Review class """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Tests for the Review class """
    def test_docstrings(self):
        """ test for the docstrings within the BaseModel class """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_inheritance(self):
        """ test that Review inherits from BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_str(self):
        """ test the __str__ method for Review """
        my_review = Review()
        s = "[{}] ({}) {}".format(my_review.__class__.__name__,
                                  my_review.id, my_review.__dict__)
        self.assertEqual(my_review.__str__(), s)

    def test_class_attributes(self):
        """ test the class attributes for Review """
        self.assertIs(type(Review.place_id), str)
        self.assertEqual(Review.place_id, "")
        self.assertIs(type(Review.user_id), str)
        self.assertEqual(Review.user_id, "")
        self.assertIs(type(Review.text), str)
        self.assertEqual(Review.text, "")
