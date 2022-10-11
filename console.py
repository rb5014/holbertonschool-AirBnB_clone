#!/usr/bin/python3
'''Module for the python interpreter'''


import cmd


class HBNBCommand(cmd.Cmd):
    '''Class used for command prompt'''

    prompt = '(hbnb) '
    intro = ('\n' + '\x1b[6;37;41m' + 'Welcome to the HBNB command interpreter:' 
             + '\x1b[0m' + '\n')

    def do_quit(self, line):
        '''Exit Prompt'''
        return True

    def do_EOF(self, line):
        '''Exit Prompt'''
        return True

    def emptyline(self):
        '''Do nothing if ENTER is pressed without command'''
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
