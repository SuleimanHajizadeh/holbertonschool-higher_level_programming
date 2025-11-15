#!/usr/bin/python3
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
