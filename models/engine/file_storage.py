#!/usr/bin/env python3
"""
A module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    A class that serializes instances to a JSON file
    and deserializes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serialize __objects to the JSON file """
        with open(self.__file_path, mode="w") as file:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)
    
    def reload(self):
        """ Deserializes JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                my_obj = json.load(file)
            for key in my_obj:
                self.__objects[key] = classes[my_obj[key]["__class__"]](**my_obj[key])
        except:
            pass
