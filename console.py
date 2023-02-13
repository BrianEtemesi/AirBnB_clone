#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
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

    def do_show(self, arg):
        """
        prints the string representation of an instance based
        on the class name and id
        """
        if arg:

            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            print(value)
                            return
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        deletes an instance based on name and id
        updates the changes to the JSON file
        """

        if arg:

            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            del file_data[key]
                            return
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and ID by
        adding or updating attribute
        The changes are saved to the json file
        """
        if not arg:
            print("**class name missing**")
            return

        if arg:
            args = arg.split()
            if len(args) < 4:
                return

            class_name = args[0]
            id = args[1]
            attr_name = args[2]
            attr_value = args[3]

            if class_name not in globals():
                print(" ** Class does not exist ** ")
                return
            else:
                name_id = class_name + "." + id
                storage.reload()
                # Store reloaded data
                reloaded_data = storage.all()
                for key, value in reloaded_data.items():
                    if key == name_id:
                        instance_dict = value
                        # Add the attibute name to the dictionary and its value
                        instance_dict[attr_name] = attr_value
                        # Save the file
                        storage.save()
                        break
                    else:
                        print(" ** Key not found ** ")

    def do_all(self, arg):
        """
        prints all string representation of instances based or not
        on the class name
        """

        all_objs = storage.all()
        if arg:
            try:
                cls = globals()[arg]
                for key, value in all_objs.items():
                    if type(value) == cls:
                        print(value)
            except KeyError:
                print("** class doesn't exist **")
        else:
            for key, value in all_objs.items():
                print(value)

    def emptyline(self):
        """
        console to execute nothing when you press enter
        without an argument
        """
        pass

    def do_quit(self, line):
        """Exits the program"""
        exit(1)

    def do_EOF(self, line):
        """handles End of File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
