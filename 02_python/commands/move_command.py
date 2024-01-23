from .base_command import BaseCommand
import os
import shutil
from typing import List

class MoveCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the MoveCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Move a file or directory to another location'
        self.usage = 'Usage: mv [source] [destination]'

        # TODO 5-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        self.source = args[0] if args else None
        self.destination = args[1] if len(args) > 1 else None
        

    def execute(self) -> None:
        """
        Execute the move command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 5-2: Implement the functionality to move a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        """
        if self.source is None or self.destination is None:
            print("Error: Missing source or destination.")
            return

        if not os.path.exists(self.source):
            print(f"Error: Source '{self.source}' does not exist.")
            return

        if os.path.isfile(self.source):
            if os.path.exists(self.destination) and os.path.isdir(self.destination):
                destination_file = os.path.join(self.destination, os.path.basename(self.source))
                if "-i" in self.options:
                    if os.path.exists(destination_file):
                        overwrite = input(f"File '{destination_file}' already exists. Overwrite? (y/n): ")
                        if overwrite.lower() != "y":
                            return
                shutil.move(self.source, destination_file)
                if "-v" in self.options:
                    print(f"Moved file '{self.source}' to '{destination_file}'")
            else:
                print(f"Error: Destination '{self.destination}' is not a directory.")
        elif os.path.isdir(self.source):
            if os.path.exists(self.destination) and os.path.isdir(self.destination):
                destination_dir = os.path.join(self.destination, os.path.basename(self.source))
                if "-i" in self.options:
                    if os.path.exists(destination_dir):
                        overwrite = input(f"Directory '{destination_dir}' already exists. Overwrite? (y/n): ")
                        if overwrite.lower() != "y":
                            return
                shutil.move(self.source, destination_dir)
                if "-v" in self.options:
                    print(f"Moved directory '{self.source}' to '{destination_dir}'")
            else:
                print(f"Error: Destination '{self.destination}' is not a directory.")
        else:
            print(f"Error: Source '{self.source}' is neither a file nor a directory.")
      


    
    def file_exists(self, directory: str, file_name: str) -> bool:
        """
        Check if a file exists in a directory.
        Feel free to use this method in your execute() method.

        Args:
            directory (str): The directory to check.
            file_name (str): The name of the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        file_path = os.path.join(directory, file_name)
        return os.path.exists(file_path)

