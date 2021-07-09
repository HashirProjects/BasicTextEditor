"""Runs the command parser and handles exceptions"""
from src.command_executor import EditFile
from src.command_parser import CommandParser


if __name__ == "__main__":
    print("Welcome to the command line BasicTextEditor")
    command_executor = EditFile()
    parser = CommandParser(command_executor)
    while True:
        command = input("> ")
        if command.upper() == "EXIT":
            break
        try:
            parser.execute_command(command.split())
        except Exception as e:
            print(e)
    print("Successfully exited the program. Have a nice day!")
