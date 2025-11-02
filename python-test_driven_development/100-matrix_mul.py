#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b"""

    # 1. Validate types
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(x, (int, float)) for x in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(x, (int, float)) for x in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 2. Check if multiplication is possible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 3. Multiply matrices
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            row_result.append(s)
        result.append(row_result)

    return result
