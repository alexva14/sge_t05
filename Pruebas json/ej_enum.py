# -*- coding: utf-8 -*-
"""
ENUM
https://docs.python.org/3/library/enum.html
"""
from enum import Enum, unique, auto

@unique 
class CasaEnum(Enum):
    """ Casas de Harry Potter """
    GRYFFINDORS = 1
    SLYTHERINS = 2
    # Otra forma
    HUFFLEPUFFS = auto()
    RAVENCLAWS = auto()
    OTRA = 0

    def __str__(self):
        return 'Casa {0}'.format(str(self.name).capitalize())

""" Pruebas """
if __name__ == "__main__":
    casaActual = CasaEnum.GRYFFINDORS

    print(casaActual)
    print(casaActual.name)
    print(casaActual.value)
    
    print( repr(casaActual) )
    print( type(casaActual) )
    print( isinstance(casaActual, CasaEnum))

    print("Las casas existentes son:")
    for c in CasaEnum:
        print(c)

    print( list(CasaEnum) )
