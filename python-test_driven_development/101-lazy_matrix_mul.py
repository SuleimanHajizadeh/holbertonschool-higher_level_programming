#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Contains lazy_matrix_mul function using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Raises:
        ValueError: If scalars are passed or shapes not aligned
        TypeError: If elements are not numbers

    Returns:
        np.ndarray: Result of matrix multiplication
    """
    try:
        return np.matmul(m_a, m_b)
    except TypeError:
        # Non-numeric types
        raise TypeError("invalid data type for einsum")
    except ValueError as e:
        msg = str(e)
        # Scalar cases
        if "does not have enough dimensions" in msg or "Scalar operands" in msg:
            raise ValueError("Scalar operands are not allowed, use '*' instead")
        # Shape misalignment
        elif "mismatch in its core dimension" in msg or "shapes" in msg:
            raise ValueError(msg.replace(
                "matmul: Input operand 1 has a mismatch in its core dimension 0, "
                "with gufunc signature (n?,k),(k,m?)->(n?,m?)",
                "shapes ... not aligned"))
        else:
            raise
