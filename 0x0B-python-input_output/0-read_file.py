#!/usr/bin/python3

def read_file(filename=""):
    """
        read file and print it out
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
