#!/usr/bin/python3
def print_last_digit(i):
    ld = 0
    if i < 0:
        temp = i * -1
        ld = (temp % 10)
    elif i > 0:
        ld = (i % 10)
    print(ld, end="")
    return (ld)
