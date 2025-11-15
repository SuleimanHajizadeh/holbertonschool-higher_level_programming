#!/usr/bin/python3
"""
Bu modul faylın sonuna mətn əlavə edilməsi üçün funksiyanı ehtiva edir.
append_write funksiyası verilən mətni faylın sonuna əlavə edir və
əlavə edilmiş simvolların sayını qaytarır.
"""


def append_write(filename="", text=""):
    """
    Verilmiş mətni faylın sonuna (UTF-8) əlavə edir.
    Fayl yoxdursa yaradır.
    Əlavə edilmiş simvolların sayını qaytarır.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
