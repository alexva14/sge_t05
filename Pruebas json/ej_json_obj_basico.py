# -*- coding: utf-8 -*-
"""
JSON
https://docs.python.org/3/library/json.html?highlight=json#module-json
"""
import json

class Mago():
    TUPLASANGRE=("Pura", "Mestiza", "Nacidos de Muggles", "Otra")

    def __init__(self, pNombre, pSangre, pEspecie) -> None:
        self._nombreCompleto=pNombre
        self._sangre=pSangre
        self._especie=pEspecie
    
    @property
    def nombreCompleto(self):
        return self._nombreCompleto
    
    @property
    def sangre(self):
        return Mago.TUPLASANGRE[self._sangre]

    @property
    def especie(self):
        return self._especie

    def __str__(self):
        return "Nombre: {} (Sangre: {}. Especie: {})".format(self.nombreCompleto, self.sangre, self.especie)

def guardarJSONunMago(rutaFich, uno):
    with open(rutaFich, 'w') as f:
        json.dump(uno, f, indent=2)

def guardarJSONcoleccionMagos(rutaFich, coleccion):
    with open(rutaFich, 'w') as f:
        json.dump(coleccion, f, indent=2)

def leerJSON(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)
    return cadjson

""" Pruebas """
if __name__ == "__main__":
    minerva = Mago("Minerva McGonagall", 1, "Humana")
    sirius = Mago("Sirius Black", 0,"Animago")
    herminone = Mago("Hermione Granger", 2,"Humana")

    listaMagos=[minerva,sirius,herminone]

    #guardarJSONunMago("ficheroUnMago1.json", minerva)
    guardarJSONunMago("ficheroUnMago2.json", str(minerva))
    guardarJSONunMago("ficheroUnMago3.json", minerva.__dict__)
    guardarJSONunMago("ficheroUnMago4.json", list(minerva.__dict__.values())) #Cuidado con values() --> dict_values([..., ..., ...])

    #guardarJSONcoleccionMagos("ficheroMagos1.json", listaMagos)
    listaMagosAux=list()
    for i in listaMagos:
        listaMagosAux.append(str(i))
    guardarJSONcoleccionMagos("ficheroMagos2.json", listaMagosAux)
    listaMagosAux=list()
    for i in listaMagos:
        listaMagosAux.append(i.__dict__)
    guardarJSONcoleccionMagos("ficheroMagos3.json", listaMagosAux)
    listaMagosAux=list()
    for i in listaMagos:
        listaMagosAux.append(list(i.__dict__.values())) #Cuidado con values() --> dict_values([..., ..., ...])
    guardarJSONcoleccionMagos("ficheroMagos4.json", listaMagosAux)
    del listaMagosAux

    del listaMagos
    del minerva
    del sirius
    del herminone

    unMagoJSON3=leerJSON("ficheroUnMago3.json") 
    minerva = Mago(unMagoJSON3["_nombreCompleto"], unMagoJSON3["_sangre"], unMagoJSON3["_especie"])
    del minerva

    unMagoJSON4=leerJSON("ficheroUnMago4.json") 
    minerva = Mago(unMagoJSON4[0],unMagoJSON4[1],unMagoJSON4[2])
    del minerva

    listaMagos=list()
    listaMagoJSON3=leerJSON("ficheroMagos3.json") 
    for i in listaMagoJSON3:
        listaMagos.append(Mago(i["_nombreCompleto"], i["_sangre"], i["_especie"]))
    del listaMagos

    listaMagos=list()
    listaMagoJSON4=leerJSON("ficheroMagos4.json") 
    for i in listaMagoJSON4:
        listaMagos.append(Mago(i[0], i[1], i[2]))
