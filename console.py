#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """command processor for the AirBnb console"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        creates a new instance of BaseModel
        saves it to the json file and prints
        the id
        """
        
        if arg:
            try:
                cls = globals()[arg]
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
