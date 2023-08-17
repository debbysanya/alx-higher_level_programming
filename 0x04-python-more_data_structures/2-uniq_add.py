#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set()
    addition = 0
    for i in my_list:
        if i not in unique_values:
            addition += i
            unique_values.add(i)
    return addition

