#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write("This School is so cool!\n")
        print(content)

append_write('file_append.txt')
