#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML formatına çevirir və fayla yazır.
    
    Parametrlər:
    dictionary (dict): Serializasiya olunacaq lüğət.
    filename (str): Yazılacaq XML faylının adı.
    """
    # Mərhələ 1: Root elementi yaratmaq
    root = ET.Element('data')

    # Mərhələ 2: Hər bir açar-dəyər cütünü uşaq elementi kimi əlavə etmək
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML-də bütün dəyərlər string olur

    # Mərhələ 3: XML-i fayla yazmaq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    XML faylını oxuyur və Python lüğətinə çevirir.
    
    Parametr:
    filename (str): Oxunacaq XML faylının adı.
    
    Qayıdış:
    dict: Deserializasiya olunmuş Python lüğəti.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text  # Bütün dəyərlər string olacaq

        return data_dict

    except FileNotFoundError:
        print(f"Error: {filename} tapılmadı.")
        return None
    except ET.ParseError:
        print(f"Error: {filename} faylı düzgün XML formatında deyil.")
        return None
