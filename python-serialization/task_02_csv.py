#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və JSON formatında 'data.json' faylına yazır.
    
    Parametr:
    csv_filename (str): CSV faylının adı.
    
    Qayıdış:
    bool: Əgər çevirmə uğurludursa True, xətalı halda False.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)  # Hər sətiri dictionary kimi oxuyur
            data_list = [row for row in reader]  # Bütün sətirləri siyahıya əlavə edir

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)  # JSON faylına yazır

        return True

    except FileNotFoundError:
        print(f"Error: {csv_filename} faylı tapılmadı.")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False
