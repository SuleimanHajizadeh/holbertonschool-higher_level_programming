#!/usr/bin/python3
"""
Bu modul mətnin fayla yazılması üçün funksiyanı ehtiva edir.
write_file funksiyası verilən mətni fayla yazır və
yazılmış simvolların sayını qaytarır.
"""


def write_file(filename="", text=""):
    """
    Verilən mətni UTF-8 formatında fayla yazır.
    Fayl yoxdursa yaradır, varsa məzmunu yenidən yazır.
    Yazılmış simvolların sayını qaytarır.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
