import argparse
import logging
from utils.command_handler import CommandHandler
from utils.command_parser import CommandParser
import pdb

# TODO 1-1: Use argparse to parse the command line arguments (verbose and log_file).
# TODO 1-2: Set up logging and initialize the logger object.

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", type=bool, default=True)
parser.add_argument("--log_path", type=str, default='file_explorer.log')
args = parser.parse_args()

command_parser = CommandParser(args.verbose)
handler = CommandHandler(command_parser)

while True:
    command = input(">> ")
    handler.execute(command)