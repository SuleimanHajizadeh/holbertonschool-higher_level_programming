#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = format(a // b, '.1f')
        print("Inside result:", end='')
    except:
        result = None
        print("Inside result:", end='')
    finally:
        print(" {}".format(result))
    return result
