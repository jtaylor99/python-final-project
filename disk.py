import core


def open_file():
    with open('inventory.txt') as f:
        f.readline()
        file_info = f.readlines()

    return file_info


def write_file(file_string):
    with open(inventory.txt, 'a') as file:
        file.write(file_string)
