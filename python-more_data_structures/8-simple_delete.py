#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete key in dictionary if it exists"""
    a_dictionary.pop(key, None)
    return a_dictionary
