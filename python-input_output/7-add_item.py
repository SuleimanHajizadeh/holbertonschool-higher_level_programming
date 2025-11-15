#!/usr/bin/python3
"""
Bu skript komanda xəttindən verilən arqumentləri oxuyur,
mövcud add_item.json faylından list yükləyir,
yeni elementləri əlavə edir və yenilənmiş list-i JSON formatında
fayla yazır.
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Komanda xəttindən verilən arqumentləri list-ə əlavə edirik
items.extend(sys.argv[1:])

# Yenilənmiş list-i fayla yazırıq
save_to_json_file(items, filename)
