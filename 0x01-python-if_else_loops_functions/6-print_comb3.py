#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if (i != 8 and j != 9):
            if i != j and i < j:
                print("{}{}, ".format(i, j), end="")
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
