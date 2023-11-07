#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """unction that writes a string to a text file
    (UTF8) and returns the number of characters """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
