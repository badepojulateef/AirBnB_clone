#!/usr/bin/python3
"""
module containing the FileStorage class
"""
import json


class FileStorage:
    """
    class to serialize/deserialize instances to/from JSON files
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        set in __objects the obj with key `<obj class name>.id`
        Args:
            obj: the object to set in __objects
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serialize __objects to the JSON file (path: __file_path)
        """
        dct = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dct, f)

    def reload(self):
        """
        deserialize the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise do nothing)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                      "City": City, "Amenity": Amenity, "Place": Place,
                      "Review": Review}
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                dct = json.load(f)
                for key, value in dct.items():
                    cls = class_dict[value["__class__"]]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
