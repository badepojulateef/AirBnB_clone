#!/usr/bin/python3
""" command interpreter for the AirBnB clone """
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity, "Place": Place,
              "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - custom Cmd class for the HBNB console
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """ override the emptyline method """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, or a subclass of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in class_dict:
            print("** class name doesn't exist **")
            return
        obj = class_dict[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Print the representation of an instance
        based on the class name and id
        """
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in class_dict:
            print("** class name doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in class_dict:
            print("** class name doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances
        based or not on the class name
        """
        if not arg:
            print(list(x.__str__() for x in storage.all().values()))
            return
        elif arg not in class_dict:
            print("** class name doesn't exist **")
            return
        print([x.__str__()
              for x
              in storage.all().values()
              if x.__class__.__name__ == arg])

    def do_update(self, arg):
        """
        Update an instance based on the class name or
        id by adding/updating attributes
        """
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in class_dict:
            print("** class name doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return
        attr = args[2]
        value = args[3]
        if value[0] == "\"" and value[-1] == "\"":
            setattr(obj, attr, value[1:-1])
        elif "." in value:
            setattr(obj, attr, float(value))
        else:
            setattr(obj, attr, int(value))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()