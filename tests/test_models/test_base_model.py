#!/usr/bin/env python3
""" A module that contains the test suite for the BaseModel class """

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ The test suite for models.base_model.BaseModel """

    def test_3_init(self):
        """ Tests the instantiation of the BaseModel class """
        base_model = BaseModel()
        # type of b
        self.assertEqual(str(type(base_model)),
                         "<class 'models.base_model.BaseModel'>")
        # b is instance of BaseModel
        self.assertIsInstance(base_model, BaseModel)
        # b is subclass of BaseModel
        self.assertTrue(issubclass(type(base_model), BaseModel))

    def test_3_init_with_no_args(self):
        pass

    def test_3_init_with_many_args(self):
        """ Test __init__() with many arguments """
        # base_model = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8 ,9)

    def test_3_attributes(self):
        """
        Checks that instance of BaseModel has attribute(s) initialization
        """
        base_model = BaseModel()
        # self.assertTrue(hasattr(base_model))

    def test_3_if_BaseModal_has_id_attribute(self):
        """  """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))

    def test_3_if_id_attribute_of_BaseModal_is_unique(self):
        """ Checks """
        # Check for two instances
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        base_model1.id = base_model2.id
        # Check for 1000 instances
        b = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(b)), len(b))

    def test_3_str_representation(self):
        """ Checks if the string representation is appropriate """
        base_model = BaseModel()
        self.assertEqual(
                str(base_model),
                "[BaseModel] ({}) {}".format(
                        base_model.id, base_model.__dict__
                    )
                )

    def test_3_initial_creation(self):
        """  """
        base_model = BaseModel()
        self.assertEqual(
                base_model.created_at.microsecond,
                base_model.updated_at.microsecond
                )

    def test_3_save(self):
        """ """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(
                base_model.created_at,
                base_model.updated_at
                )

    def test_3_to_dict(self):
        base_model = BaseModel()
        my_model = base_model.to_dict()
        self.assertEqual(my_model["id"], base_model.id)
        self.assertEqual(
                my_model["created_at"],
                base_model.created_at.isoformat()
                )
        self.assertEqual(
                my_model["updated_at"],
                base_model.updated_at.isoformat()
                )


if __name__ == "__main__":
    unittest.main()
