#!/usr/bin/python3
"""
Bu modul Student class-ını ehtiva edir.
Student class-ı tələbənin first_name, last_name və age atributlarını saxlayır.
to_json metodu obyektin dictionary nümayəndəliyini qaytarır.
attrs parametri ilə yalnız seçilmiş atributlar qaytarıla bilər.
reload_from_json metodu JSON dictionary ilə obyektin atributlarını yeniləyir.
Diskə saxlama və yükləmə üçün JSON serializasiya ilə istifadə edilə bilər.
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
        Əgər attrs listdirsə, yalnız bu listdəki atributlar daxil edilir.
        Əks halda, bütün atributlar qaytarılır.
        """
        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered
        return self.__dict__.copy()

    def reload_from_json(self, json_dict):
        """
        Obyektin atributlarını JSON dictionary ilə yeniləyir.
        Yalnız obyektin mövcud atributları dəyişir.
        json_dict: dictionary tipində, açarlar atribut adları,
        dəyərlər isə atribut dəyərləri olmalıdır.
        """
        if isinstance(json_dict, dict):
            for key, value in json_dict.items():
                if key in self.__dict__:
                    setattr(self, key, value)
