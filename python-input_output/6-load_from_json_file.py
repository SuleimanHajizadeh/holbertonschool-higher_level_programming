#!/usr/bin/python3
"""
Bu modul JSON faylından Python obyektini yaradan funksiyanı ehtiva edir.
load_from_json_file funksiyası fayldakı JSON məlumatını Python data
strukturuna çevirir.
"""

import json


def load_from_json_file(filename):
    """
    Verilmiş JSON faylını oxuyur və Python obyektinə çevirir.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
