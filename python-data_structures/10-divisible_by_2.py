#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    i = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list += [True]
        else:
            new_list += [False]
    return new_list
