#!/usr/bin/python3
# 100-my_int.py

"""Defines a MyInt class that inverts == and != operators."""


class MyInt(int):
    """Rebel integer: inverts equality operators."""

    def __eq__(self, other):
        """Inverted equality: True if values are NOT equal."""
        return int(self) != other

    def __ne__(self, other):
        """Inverted inequality: True if values are equal."""
        return int(self) == other
