from View import View
from FileHandler import FileHandler
from ClassFinder import ClassFinder
from PEP8Converter import PEP8Converter
from CommandLineInterpreter import CommandLineInterpreter


class Controller:

    def __init__(self, ClassFinder: object, View: object) -> None:
        self.my_class_finder = ClassFinder
        self.view = View
        self.all_my_classes = []

    def start_menu(self) -> None:
        incorrect_input = True
        while incorrect_input:
            View.print_menu()
            user_input = input("Please enter your input: ")

            # Press 1 to load your text file
            if user_input == "1":
                file_data = FileHandler.read_file()

            # Press 2 to write from plantuml text to python code
            elif user_input == "2":
                self.my_class_finder.find_class(self, file_data)
                self.my_class_finder.relationship_finder(self, file_data)
                self.all_my_classes = self.my_class_finder.get_all_my_classes(self)
                directory_name = FileHandler.choose_directory()
                for a_plant_class in self.all_my_classes:
                    print(a_plant_class, " ", a_plant_class.relationship)
                    content = PEP8Converter.create_class(a_plant_class)
                    FileHandler.write_file(directory_name, content, a_plant_class)

            # Press 3 to start command line interpreter
            elif user_input == "3":
                self.command_line_interpreter()

            # Awaiting option
            elif user_input == "4":
                pass

            # Exit
            elif user_input == "5":
                incorrect_input = False
                print("\ngoodbye..\n")

            else:
                input("\nWrong option. Press enter to try again...")

    def command_line_interpreter(self):
        cmd = CommandLineInterpreter()
        cmd.cmdloop()



if __name__ == "__main__":
    my_class_finder = ClassFinder()
    controller = Controller(ClassFinder, View)
    controller.start_menu()
