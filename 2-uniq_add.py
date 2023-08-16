#!/usr/bin/python3

def uniq_add(my_list=[]):
    temp_list = []
    uniq_sum = 0

    for element in my_list:
        if element not in temp_list:
            temp_list.append(element)
    for element in temp_list:
        uniq_sum = uniq_sum + element

    return (uniq_sum)
