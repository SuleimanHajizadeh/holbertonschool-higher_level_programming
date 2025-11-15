#!/usr/bin/python3
"""
Bu modul Python obyektinin JSON nümayəndəliyini qaytaran funksiyanı ehtiva edir.
to_json_string funksiyası verilmiş obyektin JSON formatında stringini qaytarır.
"""

import json


def to_json_string(my_obj):
    """
    Verilmiş Python obyektinin JSON formatında stringini qaytarır.
    """
    return json.dumps(my_obj)
