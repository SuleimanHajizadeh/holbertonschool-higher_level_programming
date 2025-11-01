#!/usr/bin/python3
"""Module for dividing all elements of a matrix by a number"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div

    matrix must be a list of lists of integers/floats
    Each row must be of the same size
    div must be a number different from 0
    Returns a new matrix with all values divided and rounded to 2 decimals
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
