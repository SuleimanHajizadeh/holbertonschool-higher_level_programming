#!/usr/bin/python3
"""
Bu modul faylda hər sətrdə müəyyən string axtarıb, onun ardınca
başqa bir sətir əlavə edən funksiyanı ehtiva edir.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    filename: fayl adı
    search_string: axtarılan string
    new_string: əlavə olunacaq string

    Faylda hər search_string-i ehtiva edən sətrin ardınca
    new_string əlavə edir.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
