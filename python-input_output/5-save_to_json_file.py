#!/usr/bin/python3
"""
Bu modul Python obyektini JSON formatında fayla yazan funksiyanı ehtiva edir.
save_to_json_file funksiyası verilmiş obyektin JSON nümayəndəliyini
müəyyən edilmiş fayla yazır.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Verilmiş Python obyektini JSON formatında fayla yazır.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
