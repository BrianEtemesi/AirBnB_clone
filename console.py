#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """command processor for the AirBnb console"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        creates a new instance of BaseModel
        saves it to the json file and prints
        the id
        """
        cls = globals()[arg]
        new_obj = cls()
        print(new_obj)

    def emptyline(self):
        """console to execute nothing when you press enter without an argument"""
        pass

    def do_quit(self, line):
        """Exits the program"""
        exit(1)
    
    def do_EOF(self, line):
        """handles End of File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

