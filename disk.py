import core
from datetime import datetime


def open_file(file_name):
    with open(file_name) as f:
        f.readline()
        file_info = f.readlines()

    return file_info


def read_history():
    with open('history.txt', 'r') as file:
        air = file.read()
        lines = air.split('\n')
        st = ''
        for line in lines:
            st += f'{line}\n'
        return st.lstrip()


def write_the_history(text):
    with open('history.txt', 'a') as file:
        file.write(text)


def total_revenue():
    total = 0
    with open('history.txt', 'r') as file:
        for line in file:
            line = line.split(',')
            total += float(line[3])
    return total


def write_file(file_string, file_name):
    with open(file_name, 'w') as file:
        file.write(file_string)
