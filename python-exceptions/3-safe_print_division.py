#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result, handling division by zero."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
