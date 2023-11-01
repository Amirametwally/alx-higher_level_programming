#!/usr/bin/python3
"""function that prints a squqre with the charachter #"""


def print_square(size):
    """function that print a square with the character"""

    if not isinstance(size, int):
        raise TypeError("size must be an intger")
    if size < 0:
        raise ValueError("size must be >=0")

    for i in range(size):
        print("#" * size)
