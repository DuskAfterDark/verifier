import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

ALLOWED_FILES = {'Loader.exe', 'server.py', 'client.py'}
REQUIRED_FOLDERS = {'scripts'}
IGNORED_ITEMS = {'runner.py'}

def verify_directory():
    current_directory = os.getcwd()
    for folder in REQUIRED_FOLDERS:
        folder_path = os.path.join(current_directory, folder)
        if not os.path.isdir(folder_path):
            print(f"{Fore.RED}Required folder '{folder}' is missing in {current_directory}.")
            sys.exit(1)
    
    for folder in REQUIRED_FOLDERS:
        folder_path = os.path.join(current_directory, folder)
        for file in os.listdir(folder_path):
            if file in IGNORED_ITEMS:
                continue
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file not in ALLOWED_FILES:
                print(f"{Fore.RED}Unrecognized file detected: {Style.BRIGHT}{file}{Style.RESET_ALL}. Example: {file_path}")
                sys.exit(1)
    
    for file in os.listdir(current_directory):
        if file in IGNORED_ITEMS:
            continue
        file_path = os.path.join(current_directory, file)
        if os.path.isfile(file_path):
            if file not in ALLOWED_FILES:
                print(f"{Fore.RED}Unrecognized file detected: {Style.BRIGHT}{file}{Style.RESET_ALL}. Example: {file_path}")
                sys.exit(1)
    
    print(f"{Fore.GREEN}Verification successful for directory: {current_directory}")

if __name__ == "__main__":
    verify_directory()
