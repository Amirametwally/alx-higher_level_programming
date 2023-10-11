#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_list = list(a_dictionary)
    dic_list.sort()
    for i in dic_list:
        print(f"{i} : {a_dictionary.get(i)}")
