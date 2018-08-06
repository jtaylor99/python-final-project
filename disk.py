import core
from datetime import datetime


def open_file():
    with open('inventory.txt') as f:
        f.readline()
        file_info = f.readlines()

    return file_info


def write_the_history(user_name, selection):
    text = f'{user_name.upper()} checked out {selection} at {datetime.now()}\n'
    with open('history.txt', 'a') as file:
        file.write(text)


def write_file(file_string):
    with open('inventory.txt', 'a') as file:
        file.write(file_string)
