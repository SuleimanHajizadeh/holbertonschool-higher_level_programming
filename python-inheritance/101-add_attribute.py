#!/usr/bin/python3
# 101-add_attribute.py

"""Function that adds a new attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if possible.

    Raises:
        TypeError: if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
