#!/usr/bin/python3
'''Module for the python interpreter'''


import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import re
from errors import Errors_
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
        # ex: State name="California" =>  # ('State', 'name="California"')
        tuple_arg = tuple(arg.split())

        # dict that will store all the key/value pairs
        dict_attr = {}
        
        # loop on args to add key/value pairs to the dict of attributes
        for elem in tuple_arg:
            # same as: if not first element(we don't want to add
            # the classname to the dict of attributes)
            if '=' in elem:
                # ex: 'name="California"' => ['name', '"California"']
                elem = elem.split('=')
                elem[1] = elem[1].replace('_', ' ')
                # new_elem will get a new version of elem[1] with escape
                # '\' before double quotes
                new_elem = ''
                for i, val in enumerate(elem[1]):
                    if val == '"' and i > 0 and i < len(elem[1]) - 2:
                        new_elem += '\\'
                    new_elem += val
                # add the key/value pair to the dict
                # ex: dict[name] = "California"
                print(new_elem)
                dict_attr[elem[0]] = new_elem
        # create, save and print the id of the new object if no errors
        if Errors_.error_checker("create", tuple_arg[0]) is True:
            b = eval(f"{tuple_arg[0]}()")
            b.save()
            print(b.id)

        # loop on dict of attributes to call do_update for each key/value pair
        for key, val in dict_attr.items():
            self.do_update(f"{tuple_arg[0]} {b.id} {key} {val}")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        if Errors_.error_checker("show", arg) is True:
            tuple_args = tuple(arg.split())
            print(d[f"{tuple_args[0]}.{tuple_args[1]}"])

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name, each case with different methods
        """
        if not arg:
            self.print_all_inst()
        else:
            self.print_cls_inst(arg)

    def print_all_inst(self):
        """CALLED BY do_all
        Return a list of  all string representation of all instances
        """
        list_obj = []
        for obj_id in d:
            list_obj.append(str(d[obj_id]))
        print(list_obj)

    def print_cls_inst(self, arg):
        """CALLED BY do_all
        Return all string representation of all instances OF A CLASS
        """
        list_obj = []
        if Errors_.error_checker("all", arg) is True:
            for obj_id in d:
                if arg + "." in obj_id:
                    list_obj.append(str(d[obj_id]))
            print(list_obj)

    def do_destroy(self, arg):
        tuple_arg = tuple(arg.split())
        if Errors_.error_checker("destroy", arg) is True:
            del d[f"{tuple_arg[0]}.{tuple_arg[1]}"]
            storage.save()

    def do_count(self, arg):
        """Count and print the number of instances of a class
        """
        nb_instances = 0
        if Errors_.error_checker("count", arg) is True:
            for obj_id in d:
                if arg + "." in obj_id:
                    nb_instances += 1
            print(nb_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = re.split('[ "]', arg)
        args = [val for val in args if val]
        if Errors_.error_checker("update", arg) is True:
            for inst in d:
                if args[1] in inst:
                    obj = d[inst]
            l_dict = {args[2]: args[3]}
            obj.update(**l_dict)
            storage.save()

    def default(self, line: str) -> None:
        """Default behavior when command prefix not recognized
        Use function select_func to check if function is in
        format "class.func" or "class.show('someid'), etc
        """
        try:
            args = re.split(r"['\":)(,.\s}{]\s*", line)
            args = [arg for arg in args if arg]
            self.select_func(args)
        except Exception:
            return super().default(line)

    def select_func(self, args):
        """Multiple try except to start functions
        """
        func = args[1]
        cls = args[0]
        if len(args) > 2:
            id = args[2]
        attr_name = []  # attr_name and attr_list stored in lists
        for i in range(0, len(args[3:]), 2):
            attr_name.append(args[3+i])
        attr_val = []
        for i in range(0, len(args[4:]), 2):
            attr_val.append(args[4+i])

        if func in ("all", "create", "count"):
            eval(f"self.do_{func}('{cls}')")

        if func in ("show", "destroy"):
            eval(f"self.do_{func}('{cls} {id}')")

        if func == "update":  # update requires loop over maybe multiple vals
            for i in range(len(attr_val)):
                self.do_update(f"{cls} {id} {attr_name[i]} {attr_val[i]}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
