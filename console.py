#!/usr/bin/python3
'''Module for the python interpreter'''


import cmd
from models.base_model import BaseModel
from models import storage
import inspect

d = storage.all()  # avoid to write the method everytime


class HBNBCommand(cmd.Cmd):
    '''Class used for command prompt'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Exit Prompt'''
        return True

    def do_EOF(self, line):
        '''Exit Prompt'''
        return True

    def emptyline(self):
        '''Do nothing if ENTER is pressed without command'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: $ create BaseModel
            If the class name is missing:
            print ** class name missing ** (ex: $ create)
            If the class name doesn’t exist:
            print ** class doesn't exist ** (ex: $ create MyModel)'''
        if self.error_checker("create", arg) is True:
            b = eval(f"{arg}()")
            b.save()
            print(b.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        if self.error_checker("show", arg) is True:
            tuple_args = tuple(arg.split())
            print(d[f"{tuple_args[0]}.{tuple_args[1]}"])

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name
        """
        list_obj = []
        if not arg:
            for obj_id in d:
                list_obj.append(str(d[obj_id]))
            print(list_obj)
        else:
            if self.error_checker("all", arg) is True:
                for obj_id in d:
                    if arg + "." in obj_id:
                        list_obj.append(str(d[obj_id]))
                print(list_obj)

    def do_destroy(self, arg):
        l_arg = tuple(arg.split())
        if self.error_checker("destroy", arg) is True:
            del d[f"{l_arg[0]}.{l_arg[1]}"]

    def error_checker(self, cmd_name, arg):
        """Select the error handlers corresponding
        """
        tuple_args = tuple(arg.split())

        if self.class_checker(cmd_name, tuple_args) is False:
            return False
        if cmd_name != 'create' and cmd_name != "all":
            if self.id_checker(tuple_args) is False:
                return False
        if cmd_name == 'update':
            if self.attribute_checker(tuple_args) is False:
                return False
        return True

    def class_checker(self, cmd_name, tuple_args):
        """ Validate first arg if its a class
        If cmd_name is all, only check tuple_args[0] if the arg[0] exists
        in the list (meaning len(tuple_args) > 0)
        """
        if len(tuple_args) == 0 and cmd_name != "all":
            print("** class name missing **")
            return False
        if cmd_name != "all" or len(tuple_args) > 0:
            try:
                inspect.isclass(eval(tuple_args[0]))
            except Exception:
                print("** class doesn't exist **")
                return False
        return True

    def id_checker(self, tuple_args):
        """Validate second arg if the id  matches an object
        """
        if len(tuple_args) < 2:
            print("** instance id missing **")
            return False
        if tuple_args[0] + "." + tuple_args[1] not in storage.all():
            print("** no instance found **")
            return False
        return True

    def attribute_checker(self, tuple_args):
        """Validate third arg and fourth arg
        if the attribute name and attribute value are valid
        """
        if len(tuple_args) < 3:
            print("** attribute name missing **")
            return False
        if len(tuple_args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
