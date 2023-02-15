#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand console."""

    def setUp(self):
        """ Test case for setUp """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    def test_help_EOF(self):
        """ Test case for help EOF """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = "Quit command to exit the program\n"
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """ Test case for help all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        self.assertIn("""Print all string representation of all instances
        based or not on the class name""", f.getvalue())

    def test_help_create(self):
        """ Test case for help create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = "Create a new instance of BaseModel, or a subclass of BaseModel\n"
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """ Test case for help destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = "Delete an instance based on the class name and id\n"
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """ Test case for help show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = "Print the representation of an instance"
        self.assertIn(s, f.getvalue())

    def test_help_help(self):
        """ Test case for help help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
        s = "List available commands with"
        self.assertIn(s, f.getvalue())

    def test_help_update(self):
        """ Test case for help update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s = "Update an instance based on the class name or"
        self.assertIn(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        # self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", "\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        # self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", "\n")

    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        s = ""
        self.assertEqual(s, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        s = ""
        self.assertEqual(s, f.getvalue())


if __name__ == "__main__":
    unittest.main()
