#!/usr/bin/env python3
""" A Test Suite for FileStorage in models/file_storage.py """

import os
import json
import unittest
import re
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """ Test cases for FileStorage class init """


    def resetStorage(self):
        """ Reset Storage """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    
    def test_5_init(self):
        """ Init """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_5_init_with_no_args(self):
        """ Test for init without args """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_5_init_with_many_args(self):
        """ Test init for many args """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    def test_5_init_attributes(self):
        """ Test init for many args """
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_5_file_path_is_a_private_class_attr(self):
        """ Test if file path is a private attribute """
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_5_objects_is_a_private_class_attr(self):
        """ Test if file path is a private attribute """
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))


class TestFileStotageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    def setUp(self):
        """ help/utility test for reload function """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def tearDown(self):
        """ Code to execute after tests are executed """
        # remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_5_all(self):
        """ Test all() of the FileStorage class """
        self.assertTrue(type(storage.all() is dict))

        # What if arg is passed? Ohh! TypeError, do your job!
        with self.assertRaises(TypeError) as e:
            storage.all(None)

    def test_5_new(self):
        """ Test new() of the FileStorage class """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_place = Place()
        dummy_city = City()
        dummy_amenity = Amenity()
        dummy_review = Review()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + dummy_bm.id,
                      storage.all().keys())
        self.assertIn(dummy_bm, storage.all().values())
        self.assertIn("User." + dummy_user.id, storage.all().keys())
        self.assertIn(dummy_user, storage.all().values())
        self.assertIn(dummy_state, storage.all().values())
        self.assertIn("Place." + dummy_place.id, storage.all().keys())
        self.assertIn(dummy_place, storage.all().values())
        self.assertIn("City." + dummy_city.id, storage.all().keys())
        self.assertIn(dummy_city, storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id,
                      storage.all().keys())
        self.assertIn(dummy_amenity, storage.all().values())
        self.assertIn("Review." + dummy_review.id,
                      storage.all().keys())
        self.assertIn(dummy_review, storage.all().values())

        # What if more than one arg were passed to this guy?
        # TypeError, we need you here!
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

        # What if None was passed? That guy needs learn a lesson...
        # AttributeError, will you join us?
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_5_save(self):
        """ Test cases for save method """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.save()

        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # What happens when an arg is passed? TypeError has been my agent!
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_5_method(self):
        """ Test cases for reload() """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        storage.all()
        storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)

        # What happens when an arg is passed? TypeError is raised
        with self.assertRaises(TypeError):
            storage.reload(None)

if __name__ == "__main__":
    unittest.main()
