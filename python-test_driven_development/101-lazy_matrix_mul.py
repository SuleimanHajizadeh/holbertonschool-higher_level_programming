#!/usr/bin/python3
# Try to import NumPy, but allow the module to work without it (IDE/linter may not resolve numpy)
try:
    import numpy as np
except Exception:
    np = None

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy when available, otherwise use a pure-Python fallback.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Result of matrix multiplication.

    Raises:
        ValueError: If m_a or m_b is empty or if matrices cannot be multiplied.
    """

    # If NumPy is available, prefer it for correctness/performance
    if np is not None:
        try:
            return np.dot(m_a, m_b).tolist()
        except ValueError:
            raise ValueError("m_a and m_b can't be multiplied")

    # Basic validation and pure-Python multiplication fallback
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Determine dimensions (assumes well-formed matrices)
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute multiplication
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            s = 0
            for k in range(cols_a):
                s += m_a[i][k] * m_b[k][j]
            result[i][j] = s
    return result

if __name__ == "__main__":
    # You can add test cases here or use the provided 101-main.py script for testing
    pass
