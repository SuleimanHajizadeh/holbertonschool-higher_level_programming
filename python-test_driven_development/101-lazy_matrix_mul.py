#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy, with Holberton error handling.

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second matrix

    Raises:
        TypeError: for non-list or non-number elements, unequal row lengths
        ValueError: for empty matrices or incompatible shapes

    Returns:
        list: resulting matrix
    """

    # Validate types
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    # Check rows have same size
    if len({len(row) for row in m_a}) > 1:
        raise TypeError("each row of m_a must should be of the same size")
    if len({len(row) for row in m_b}) > 1:
        raise TypeError("each row of m_b must should be of the same size")

    # Check all elements are numbers
    for row in m_a:
        if any(not isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if any(not isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # Perform multiplication
    try:
        return np.matmul(m_a, m_b).tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
