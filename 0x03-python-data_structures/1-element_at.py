#!/usr/bin/python3

def element_at(my_list, idx):
    """Prints an element of
    a list based on the index
    """
    for i in range(len(my_list)):
        if i >= 0 and i < len(my_list):
            if i == idx:
                print("{}".format(my_list[i]))
        else:
            print(None)
