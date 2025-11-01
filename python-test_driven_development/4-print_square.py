#!/usr/bin/python3
"""Module that prints a square with the character #"""

def print_square(size):
    """Prints a square of size 'size' using the character #

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is <= 0

    Example:
    >>> print_square(2)
    ##
    ##
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be > 0
    >>> print_square("3")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be > 0")
    for _ in range(size):
        print("#" * size)
