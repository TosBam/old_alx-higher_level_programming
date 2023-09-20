#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    A function to write into an existing file
    Args:
        filename: the file to write into.
        text: the string to write into a file.
    Returns:
        To return the written string
    """

    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write("This School is so cool!\n")
        print(content)

append_write('file_append.txt')
