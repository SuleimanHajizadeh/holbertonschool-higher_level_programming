#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy, with Holberton error handling."""

    # Reject non-lists (Holberton expects: ValueError "Scalar operands...")
    if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Must be list of lists
    if any(not isinstance(row, list) for row in m_a):
        raise ValueError("m_a and m_b can't be multiplied")
    if any(not isinstance(row, list) for row in m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Empty matrices → Holberton expects ValueError "m_a and m_b can't be multiplied"
    if m_a == [] or m_b == []:
        raise ValueError("m_a and m_b can't be multiplied")
    if m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a and m_b can't be multiplied")

    # All rows must have the same size
    if len({len(r) for r in m_a}) > 1:
        raise ValueError("m_a and m_b can't be multiplied")
    if len({len(r) for r in m_b}) > 1:
        raise ValueError("m_a and m_b can't be multiplied")

    # Reject non-number elements before NumPy touches them
    for row in m_a:
        for v in row:
            if not isinstance(v, (int, float)):
                raise TypeError("m_a and m_b can't be multiplied")
    for row in m_b:
        for v in row:
            if not isinstance(v, (int, float)):
                raise TypeError("m_a and m_b can't be multiplied")

    # Finally attempt NumPy multiplication
    try:
        return np.matmul(m_a, m_b).tolist()
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
