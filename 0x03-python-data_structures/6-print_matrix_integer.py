#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            if j != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][col]), end="")
        print()
