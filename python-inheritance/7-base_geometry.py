#!/usr/bin/python3
"""Module that defines BaseGeometry class with area and integer_validator methods."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter (for error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        # İlk hərfi böyük et ki, doctest-lə uyğun olsun
        cap_name = name[0].upper() + name[1:] if name else name

        if type(value) is not int:  # bool da daxil deyil
            raise TypeError(f"{cap_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{cap_name} must be greater than 0")
