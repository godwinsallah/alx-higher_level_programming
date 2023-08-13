#!/usr/bin/python3

def element_at(my_list, idx):
    """Prints an element of
    a list based on the index
    """
        if idx < 0 or idx >= len(my_list):
            return (None)
        return (my_list[idx])
