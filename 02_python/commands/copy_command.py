from .base_command import BaseCommand
import os
import shutil
from typing import List

class CopyCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the CopyCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Copy a file or directory to another location'
        self.usage = 'Usage: cp [source] [destination]'

        # TODO 6-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        # ...
        self.source = args[0] if args else None
        self.destination = args[1] if len(args) > 1 else None

    def execute(self) -> None:
        """
        Execute the copy command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 6-2: Implement the functionality to copy a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        You may use the file_exists() method to check if the destination file already exists.
        """
        if self.source and self.destination:
            if self.file_exists(self.destination, os.path.basename(self.source)):
                if '-i' in self.options:
                    overwrite = input("File already exists. Do you want to overwrite it? (y/n): ")
                    if overwrite.lower() != 'y':
                        print("cp: operation canceled")
                        return
                if '-v' in self.options:
                    print(f"Copying {self.source} to {self.destination}...")
                try:
                    shutil.copy2(self.source, self.destination)
                    print("Copy completed.")
                except Exception as e:
                    print(f"An error occurred while copying: {str(e)}")
            else:
                print("Destination directory does not exist.")
        else:
            print("Please provide both source and destination arguments.")

        try:
            # Perform the copy operation
            shutil.copy(self.source, self.destination)
            print(f"Copied '{self.source}' to '{self.destination}'")

        except Exception as e:
            print(f"cp: an error occurred during the copy operation: {e}")


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