#!/usr/bin/python3
"""Base geometry module."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Raise an exception: area() not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
