#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """command processor for the AirBnb console"""
    prompt = '(hbnb)'
    intro = 'Welcome to your AirBnb back-end console'

    def do_prompt(self, line):
        """change interactive prompt"""
        self.prompt = line

    def do_EOF(self, line):
        """handles End of File"""
        return True

    def do_quit(self, line):
        """Exits the program"""
        pass;


if __name__ == '__main__':
    HBNBCommand().cmdloop()
