#!/usr/bin/python3
"""
Bu modul Student class-ını ehtiva edir.
Student class-ı tələbənin first_name, last_name və age atributlarını saxlayır
və to_json metodu ilə obyektin dictionary nümayəndəliyini qaytarır.
attrs parametri ilə yalnız seçilmiş atributlar qaytarıla bilər.
"""


class Student:
    """
    Student class-ı tələbənin məlumatlarını saxlayır.
    """

    def __init__(self, first_name, last_name, age):
        """
        Student obyektini first_name, last_name və age ilə yaradır.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Obyektin atributlarını dictionary formatında qaytarır.
        If attrs is a list of strings, only attributes with names in this list are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered
        return self.__dict__.copy()
