#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j] ** 2)
        new_m.append(temp)

    return (new_m)
