# -*- coding: utf-8 -*-
"""
JSON
https://docs.python.org/3/library/json.html?highlight=json#module-json
"""
import json

class Usuario: 
    def __init__(self, dni, contrasenna, ultimoAcceso, es_admin, pago):
        self._dni=dni
        self._contrasenna=contrasenna
        self._ultimoAcceso=ultimoAcceso
        self._es_admin=es_admin
        self._corriente_pago=pago

def guardarJSONcoleccionMagos(rutaFich, coleccion):
    with open(rutaFich, 'w') as f:
        json.dump(coleccion, f, indent=2)

def leerJSON(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)
    return cadjson

""" Pruebas """
if __name__ == "__main__":
    minerva = Usuario ('11111111A','admin', '24/01/2022', True, True)
    sirius = Usuario ('22222222B','admin', '24/01/2022', True, True)
    herminone = Usuario ('fg','admin', '24/01/2022', True, True)

    listaUsuarios=[minerva,sirius,herminone]


    #guardarJSONcoleccionMagos("ficheroMagos1.json", listaMagos)
    listaUsuariosAux=list()
    for i in listaUsuarios:
        listaUsuariosAux.append(i.__dict__)
    guardarJSONcoleccionMagos("usuarios.json", listaUsuariosAux)
    
    del listaUsuariosAux

    listaMagos=list()
    listaMagoJSON3=leerJSON("usuarios.json") 
    for i in listaMagoJSON3:
        listaMagos.append(Usuario(i["_dni"], i["_contrasenna"], i["_ultimoAcceso"], i["_es_admin"], i["_corriente_pago"]))
    del listaMagos

