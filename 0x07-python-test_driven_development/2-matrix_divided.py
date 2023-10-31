#!/usr/bin/python3
"""function divides a matrix by a number
"""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by a number"""
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message_type = """matrix must be a matrix (list of lists)
    of integers/floats"""
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message_type)

    length = 0
    message_size = "Each row of the matrix must have the same size"
    for elemnts in matrix:
        if not elemnts or not isinstance(elemnts, list):
            raise TypeError(message_type)

        if length != 0 and len(elemnts) != length:
            raise TypeError(message_size)

        for number in elemnts:
            if not isinstance(number, (int, float)):
                raise TypeError(message_type)

        length = len(elemnts)

    n = list(map(lambda a: list(map(lambda b: round(b / div, 2), a)), matrix))
    return (n)
