#!/usr/bin/python3
"""
Bu modul Python obyektinin atributlarını JSON serializasiya üçün
dictionary formatında qaytaran funksiyanı ehtiva edir.
"""


def class_to_json(obj):
    """
    Verilmiş obyektin bütün atributlarını dictionary şəklində qaytarır.
    Yalnız list, dict, string, int və bool tipləri serializasiya edilir.
    """
    return obj.__dict__.copy()
