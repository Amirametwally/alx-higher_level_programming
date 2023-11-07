#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """function that returns a list of lists
    of integers representing the Pascal's triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        last_r = triangle[-1]
        r = [1] + [last_r[j-1] + last_r[j] for j in range(1, i)] + [1]
        triangle.append(r)
    return triangle
