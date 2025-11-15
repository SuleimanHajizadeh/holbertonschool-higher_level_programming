#!/usr/bin/python3
"""
Bu modul Pascal üçbucağını yaradan funksiya ehtiva edir.
pascal_triangle(n) funksiyası n sətri olan üçbucağı list of lists şəklində qaytarır.
"""


def pascal_triangle(n):
    """
    n sətri olan Pascal üçbucağını qaytarır.
    Əgər n <= 0 olarsa, boş siyahı qaytarılır.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # ilk sıra

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Yeni sıra: əvvəlcə 1 əlavə et
        row = [1]
        # Orta elementlər: əvvəlki sıradakı qonşu elementlərin cəmi
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # Sıra sonuna 1 əlavə et
        row.append(1)
        triangle.append(row)

    return triangle
