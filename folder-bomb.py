#!/usr/bin/python3

# usage: python3 folder-bomb.py NUMBER-OF-FOLDERS-TO-CREATE AND WERE TO CREATE
# example: python3 folder-bomb.py 100 /home/USER/Desktop


class Folder_Bomb:
    def __init__(self, folders_limit, target_directory):
        self.target_directory = target_directory 
        self.foldername = 1
        self.created_folders = 0
        self.folders_limit = folders_limit
        self.print_logs = True
        self.print_consequence = True

    def usage(self):
        print("Usage: python3 folder-bomb.py NUMBER-OF-FOLDERS-TO-CREATE DIRECTORY-WHERE-TO-CREATE-THEM")

    def die(self):
        sys.exit()

    def func_print_consequence(self):
        print()

        logging.info(f" --- In total: {self.created_folders} folders have been created in {self.target_directory}")

    def spam(self):
        os.mkdir(f"{self.target_directory}/{self.foldername}") # if you use Windows, you have to change: ' / ' to ' \\ '

        if self.print_logs:
            logging.info(f"--- Folder '{self.foldername}' created in {self.target_directory}")

        self.foldername += 1
        self.created_folders += 1

    def if_keyboard_interrupt(self):
        print()
        if self.print_logs:
            print
            logging.info("--- Program stopped\n")

        if self.print_consequence:
            spam.func_print_consequence()

        spam.die()

    def if_file_exists_error(self):
        logging.info(f"--- Folder: '{self.foldername}' already exists in {self.target_directory}")

        self.created_folders = self.created_folders
        self.foldername += 1

    def start_spam(self):
        while self.foldername <= self.folders_limit:
            
            try:
                
                spam.spam()

            except KeyboardInterrupt:
                spam.if_keyboard_interrupt()

            except FileExistsError:
                spam.if_file_exists_error()

        if self.print_consequence:
            spam.func_print_consequence()

if __name__ == '__main__':
    import os
    import logging
    import sys

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.getLogger().setLevel(logging.INFO)

    spam = Folder_Bomb(0, '...')
    try:
        folders_limit = int(sys.argv[1])
        target_directory = sys.argv[2]
    except IndexError:
        spam.usage()
        spam.die()
    else:
        spam = Folder_Bomb(folders_limit, target_directory)

    spam.start_spam()
