#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Executes a function safely, prints error to stderr if occurs."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
