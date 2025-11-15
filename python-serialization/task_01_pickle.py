#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını çap edir."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Obyekti pickle modulundan istifadə edərək fayla yazır.
        Fayl mövcud deyilsə yaradır.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Fayldan obyekt oxuyur və CustomObject instansiyası olaraq qaytarır.
        Xətalar zamanı None qaytarır.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
