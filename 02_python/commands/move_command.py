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
        self.name = 'mv'
        self.options = options
        self.source = self.args[0]
        self.destination = self.args[1]
        self.prompt = '-i' in self.options
        self.verbose = '-v' in self.options
        

    def execute(self) -> None:
        """
        Execute the move command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 5-2: Implement the functionality to move a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        """
        # Check if the source file or directory exists
        if not self.file_exists(os.getcwd(), self.source):
            print(f"Error: {self.source} does not exist.")
            return

        # Check if the destination file or directory exists
        if self.file_exists(os.getcwd(), self.destination):
            # Prompt the user before overwriting the existing file
            if self.prompt:
                response = input(f"overwrite {self.destination}? (y/n): ")
                if response.lower() != 'y'
                    
                    print("Move command cancelled.")
                    return
            # Remove the existing file or directory
            try:
                if os.path.isfile(self.destination):
                    os.remove(self.destination)
                else:
                    shutil.rmtree(self.destination)
            except Exception as e:
                print(f"Error: Failed to remove {self.destination}.")
                print(f"Reason: {str(e)}")
                return

        # Move the source file or directory to the destination
        try:
            shutil.move(self.source, self.destination)
            if self.verbose:
                print(f"Moved {self.source} to {self.destination}")
        except Exception as e:
            print(f"Error: Failed to move {self.source} to {self.destination}.")
            print(f"Reason: {str(e)}")


    
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
