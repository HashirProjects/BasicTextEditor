"""A command parser class."""

class CommandParser:
    """A class used to parse and execute a user Command."""

    def __init__(self, command_executor):
        self.command_executor = command_executor

    def execute_command(self, command):
        """
        Executes the user command.
        Raises Exception if a command cannot be parsed, or if no command is entered.
        """
        try:

            if command[0].upper() == "FIND_ALL":
                if len(command) != 2:
                    raise Exception("Please enter FIND_ALL followed by the path to the directory that you want to list the files from.")

                self.command_executor.findAllTextFiles(command[1])


            elif command[0].upper() == "CLOSE":
                self.command_executor.close()

            elif command[0].upper() == "DISPLAY":
                self.command_executor.display()

            elif command[0].upper() == "OPEN":

                if len(command) != 2:
                    raise Exception("Please enter OPEN followed by filepath to textfile.")

                self.command_executor.open(command[1])

            elif command[0].upper() == "MOVE":

                if len(command) != 2:
                    raise Exception("Please enter MOVE followed by the new file location.")

                self.command_executor.move(command[1])

            elif command[0].upper() == "HELP":
                self._get_help()
            else:
                raise Exception("Please enter a valid command, type HELP for a list of available commands.")

        except IndexError:
            print("Please enter a command, type HELP for a list of available commands.")

    def _get_help(self):
        """Displays all available commands to the user."""
        help_text = """
        Available commands:
            FIND_ALL : finds all the editable text files in the specified directory and its sub-directories 
            OPEN : opens the text file at the specified path
            CLOSE : closes and saves the text file that is currently open
            MOVE : moves the currently open text file to the specified path (directories will be created if they do not exist)
        """
        print(help_text)
