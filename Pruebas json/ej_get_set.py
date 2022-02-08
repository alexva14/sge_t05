# -*- coding: utf-8 -*-
"""
Get & Set
https://docs.python.org/3/library/functions.html#property
"""

class HechizoV1:
    def __init__(self, pNombre, pTipo, pEfecto):
        self._nombre=pNombre
        self._tipo=pTipo
        self._efecto=pEfecto
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, pNombre):
        self._nombre=pNombre

class HechizoV2:
    def __init__(self, pNombre, pTipo, pEfecto):
        self._nombre=pNombre
        self._tipo=pTipo
        self._efecto=pEfecto

class HechizoV3:
    def __init__(self, pNombre, pTipo, pEfecto):
        self._nombre=pNombre
        self._tipo=pTipo
        self._efecto=pEfecto

    def getNombre(self):
        print("Entro en get v3")
        return self._nombre

    def setNombre(self, pNombre):
        print("Entro en set v3")
        self._nombre = pNombre

    def delNombre(self):
        del self._nombre

    nombre = property(getNombre, setNombre, delNombre, "La propiedad _nombre.")

class HechizoV4:
    def __init__(self, pNombre, pTipo, pEfecto):
        self._nombre=pNombre
        self._tipo=pTipo
        self._efecto=pEfecto

    @property
    def nombre(self):
        print("Entro en get v4")
        return self._nombre
    
    @nombre.setter
    def nombre(self, pNombre):
        print("Entro en set v4")
        self._nombre = pNombre
    
    @nombre.deleter
    def nombre(self):
        del self._nombre

if __name__ == "__main__":
    #Forma 1.
    imperiusV1=HechizoV1("Imperio", "Maldición", "Control Total")
    imperiusV1.setNombre("Imperius")
    print(imperiusV1.getNombre())

    #Forma 2.
    imperiusV2=HechizoV2("Imperio", "Maldición", "Control Total") 
    setattr(imperiusV2,"_nombre", "Imperius")
    print( getattr(imperiusV2,"_nombre") )
    #Otras: delattr y hashattr

    #Forma 3.
    imperiusV3=HechizoV3("Imperio", "Maldición", "Control Total")
    imperiusV3.nombre="Imperius"
    print(imperiusV3.nombre)

    #Forma 4.
    imperiusV4=HechizoV4("Imperio", "Maldición", "Control Total")
    imperiusV4.nombre="Imperius"
    print(imperiusV4.nombre)