#!/usr/bin/python3
"""
Bu modul Student class-ını ehtiva edir.
Student class-ı tələbənin first_name, last_name və age atributlarını saxlayır
və to_json metodu ilə obyektin dictionary nümayəndəliyini qaytarır.
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

    def to_json(self):
        """
        Obyektin atributlarını dictionary formatında qaytarır.
        """
        return self.__dict__.copy()
