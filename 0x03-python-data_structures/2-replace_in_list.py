#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = 0
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx > (length - 1):
            return my_list
    for i in my_list:
        x += 1
        if idx == x:
            my_list[idx] = element
    return my_list

