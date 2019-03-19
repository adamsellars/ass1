from cmd import Cmd
from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter



class CommandLineInterpreter(Cmd):
    # Created by Adam
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.do_greet()
        self.data = ""
        self.file_handler = FileHandler()

    def do_loadfile(self, line):
        self.data = self.file_handler.read_file()

    def do_printfile(self):
        pass

    def do_greet(self):
        print("Welcome to the command line interpreter.\nType help to view available commands\n")

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

