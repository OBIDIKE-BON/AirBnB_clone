#!/usr/bin/python3
"""a module that contains the entry point of the command interpreter"""
import shlex
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


def compute_update(args, ln, v):
    if ln >= 3:
        if ln >= 4:
            v.__dict__[args[2]] = args[3]
            v.save()
            return
        else:
            print("** value missing **")
            return
    else:
        print("** attribute name missing **")
        return


def get_ids(objects):
    ids = []
    for key in objects.keys():
        ids.append(key.split('.')[1])
    return ids


def get_cls(objects):
    cls = []
    for key in objects.keys():
        cls.append(key.split('.')[0])
    return cls


cls_names = [
    'BaseModel',
    'User'
    'State',
    'City',
    'Amenity',
    'Place',
    'Review'
]


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
        elif arg not in self.cls_names:
            print("** class doesn't exist **")
        else:
            new = eval(arg + '()')
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """

        objects = storage.all()
        args = arg.split()
        cls = get_cls(objects)
        ln = len(args)
        if ln == 0:
            print('** class name missing **')
        elif args[0] not in cls:
            print("** class doesn't exist **")
        elif ln == 1:
            print("** instance id missing **")
        else:
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

        objects = storage.all()
        args = arg.split()
        cls = get_cls(objects)
        ln = len(args)
        if ln == 0:
            print('** class name missing **')
        elif args[0] not in cls:
            print("** class doesn't exist **")
        elif ln == 1:
            print("** instance id missing **")
        else:
            value = args[0] + '.' + args[1]
            for obj_id in objects.keys():
                if value == obj_id:
                    objects.pop(value)
                    storage.save()
                    break
                else:
                    print('** no instance found **')

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        """
        args = shlex.split(arg)
        objects = storage.all()
        ln = len(args)
        if ln >= 1:
            cls = get_cls(objects)
            ids = get_ids(objects)
            if args[0] in cls:
                if ln >= 2:
                    if args[1] in ids:
                        key = f"{args[0]}.{args[1]}"
                        v = objects[key]
                        return compute_update(args, ln, v)
                    else:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
                    return
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
        """

        objects = storage.all()
        my_obj = []
        if arg == '':
            for obj in objects:
                my_obj.append(str(objects[obj]))
            print(my_obj)
            return

        for k, v in objects.items():
            class_name = k.split('.')
            if arg == class_name[0]:
                my_obj.append(str(v))
        if len(my_obj) > 0:
            print(my_obj)
        else:
            print("** class doesn't exist **")

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
