#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    new_string = ''
    for i in string_list:
        if i == 'c' or i == 'C':
            continue
        new_string += i
    return new_string
