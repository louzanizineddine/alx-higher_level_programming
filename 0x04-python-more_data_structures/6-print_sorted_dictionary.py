#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sorted_dictionary = dict(sorted(a_dictionary.items()))
    for k in sorted_dictionary:
        print(f"{k}: {sorted_dictionary[k]}")
