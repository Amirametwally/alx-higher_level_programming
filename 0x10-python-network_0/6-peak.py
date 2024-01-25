#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    """function that finds a peak in a
    list of unsorted integers"""
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers[0], list_of_integers[1])
    elif n == 0:
        return None
    mid = n // 2
    if list_of_integers[mid] > list_of_integers[mid - 1] \
        and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] <= list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid+1:])
