#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini JSON faylına yazır.
    
    Parametrlər:
    data (dict): Saxlanacaq məlumat.
    filename (str): Yazılacaq JSON faylının adı.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def load_and_deserialize(filename):
    """
    JSON faylını oxuyur və Python lüğətinə çevirir.
    
    Parametrlər:
    filename (str): Oxunacaq JSON faylının adı.
    
    Qayıdış:
    dict: Deserialization edilmiş Python lüğəti.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
