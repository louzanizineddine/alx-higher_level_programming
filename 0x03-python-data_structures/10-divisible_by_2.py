#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        my_new_list = []
        for i in my_list:
            if i % 2 == 0:
                my_new_list.append(True)
            else:
                my_new_list.append(False)
        return my_new_list
    return None
