#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write("School is so cool!\n")
        print(content)

write_file("my_first_file.txt")
