# -*- coding: utf-8 -*-
"""
JSON
https://docs.python.org/3/library/json.html?highlight=json#module-json
"""
import json
from usuarios import Usuario
class Club:
    def __init__(self, nombreClub, cif):
        self._nombreClub=nombreClub
        self._cif=cif
        self._sedeSocial=None
        self._dicSocios=None
        self._listaEventos=None
        self._saldoTotal=None
        self._controlCuotas=None
        self._diccUsuarios= None
    
    def asignarListaSocios(self, diccionariosSocios):
            self._dicSocios=diccionariosSocios
        
    def asignarListaUsuarios(self, diccionarioUsuarios):
        self._diccUsuarios=diccionarioUsuarios
    
    def getUsuario(self, dni):
        return self._diccUsuarios[dni]

    def  getSocio(self, dni):
        return self._dicSocios[dni]

def guardarJSONcoleccionMagos(rutaFich, coleccion):
    with open(rutaFich, 'w') as f:
        json.dump(coleccion, f, indent=2)

def leerJSON(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)
    return cadjson

""" Pruebas """
if __name__ == "__main__":
    club= Club("Los satanases del Infierno", 13230)
    listaUsuarios=[club]


    #guardarJSONcoleccionMagos("ficheroMagos1.json", listaMagos)
    listaMagosAux=list()
    for i in listaUsuarios:
        listaMagosAux.append(i.__dict__)
    guardarJSONcoleccionMagos("club.json", listaMagosAux)
    
    del listaMagosAux

    del listaUsuarios