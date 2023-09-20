#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    A function to write into a file
    Args:
        filename: the file to write into.
        text: the string to write into a file.
    Returns:
        To return the written string
    """
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write("School is so cool!\n")
        print(content)

write_file("my_first_file.txt")
