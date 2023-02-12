#!/usr/bin/python3
"""
A module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os

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
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file """
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            my_dict = {key: value.to_dict() for key,
                       value in FileStorage.__objects.items()}
            json.dump(my_dict, file)

    def reload(self):
        """ Deserializes JSON file to __objects """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as file:
            my_obj = json.load(file)
            for key in my_obj:
                FileStorage.__objects[key] = classes[my_obj[key]["__class__"]](
                        **my_obj[key]
                        )
