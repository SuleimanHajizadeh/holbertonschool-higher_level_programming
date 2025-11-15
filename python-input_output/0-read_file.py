#!/usr/bin/python3
"""
Bu modul fayl oxumaq üçün funksiyanı ehtiva edir.
read_file funksiyası mətn faylını oxuyub ekranə çap edir.
"""


def read_file(filename=""):
    """
    Verilmiş mətn faylını (UTF-8) oxuyur və məzmununu stdout-a çap edir.
    """
    with open(filename, "r", encoding="utf-8") as f:
        # faylı oxuyuruq və ekrana yazdırırıq
        print(f.read(), end="")
