#!/usr/bin/python3

def read_file(filename=""):
    """
    a function to read a file
    args:
        filename: the file to read

    Returns: string

    """
    with open(filename, "r", encoding='utf-8') as file:

        contents = file.read()
        print(contents)

read_file("my_file_0.txt")
