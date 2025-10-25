#!/usr/bin/python3
"""Calculator functions: add, sub, mul, div."""


def add(a, b):
    """Return the addition of a and b."""
    return a + b


def sub(a, b):
    """Return the subtraction of a and b."""
    return a - b


def mul(a, b):
    """Return the multiplication of a and b."""
    return a * b


def div(a, b):
    """Return the integer division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b
