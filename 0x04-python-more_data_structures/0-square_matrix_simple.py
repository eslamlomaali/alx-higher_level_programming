#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[intt ** 2 for intt in row] for row in matrix]
    return new
