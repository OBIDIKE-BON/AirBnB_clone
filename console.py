#!/usr/bin/python3
"""a module that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """the command interpreter class inheriting from the cmd module"""

    def __init__(self):
        """initializes the intepreter instance"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, 
            saves it (to the JSON file) and prints the id
        """
        if arg == '':
            print('** class name missing **')
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new = eval(arg + '()')
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance 
            based on the class name and id
        """
        args = arg.split()
        if args[0] == '':
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")



    def emptyline(self):
        """overrides the behavior of pressing enter"""
        pass

    def do_quit(self, arg):
        """command to quit or exit the interpreter"""
        return True

    # shortcuts
    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
