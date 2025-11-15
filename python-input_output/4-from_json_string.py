#!/usr/bin/python3
"""
Bu modul JSON stringini Python obyektinə çevirən funksiyanı ehtiva edir.
from_json_string funksiyası JSON stringini Python data strukturuna çevirir.
"""

import json


def from_json_string(my_str):
    """
    Verilmiş JSON stringini Python obyektinə çevirir.
    """
    return json.loads(my_str)
