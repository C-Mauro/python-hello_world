#!/usr/bin/python3


def max_integer(my_list=[]):
    max_value = 0
    if my_list == []:
        return None
    for i in range(len(my_list)):
        if max_value < i:
            max_value = my_list[i]
    return max_value
