#!/usr/bin/python3
#2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace a specified element in the list"""

    if idx < 0 or idx >= len(my_list):
        pass
    else:
        my_list[idx] = element
    return my_list
