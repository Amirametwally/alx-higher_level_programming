#!/usr/bin/python3
"""
function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("m_a must be a list of lists")

    for element in m_b:
        if not isinstance(element, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for element in lists:
            if not type(element) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for element in lists:
            if not type(element) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for element in m_a:
        if length != 0 and length != len(element):
            raise TypeError("each row of m_a must be of the same size")
        length = len(element)

    length = 0

    for element in m_b:
        if length != 0 and length != len(element):
            raise TypeError("each row of m_b must be of the same size")
        length = len(element)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row1 = []
    i1 = 0

    for a in m_a:
        row2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                row2.append(num)
                num = 0
            else:
                i1 += 1
        row1.append(row2)

    return row1
