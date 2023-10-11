#!/usr/bin/python3
"""a module that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            value = args[0] + '.' + args[1]
            for obj_id in objects.keys():
                if value == obj_id:
                    print(objects[value])
                    break
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """

        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            value = args[0] + '.' + args[1]
            for obj_id in objects.keys():
                if value == obj_id:
                    objects.pop(value)
                    storage.save()
                    break
            else:
                print('** no instance found **')

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
