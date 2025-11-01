#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with all values squared"""
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]  # hər elementin kvadratı
        new_matrix.append(new_row)
    return new_matrix
