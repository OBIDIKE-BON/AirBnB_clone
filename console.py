#!/usr/bin/python3
"""a module that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the command interpreter class inheriting from the cmd module"""

    def __init__(self):
        """initializes the intepreter instance"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

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
