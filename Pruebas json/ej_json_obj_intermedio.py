# -*- coding: utf-8 -*-
"""
JSON
https://docs.python.org/3/library/json.html?highlight=json#module-json
"""
import json

class Magias():
    def __init__(self, pVarita, pPatronus) -> None:
        self._varita=pVarita
        self._patronus=pPatronus
    
    @property
    def varita(self):
        return self._varita

    @property
    def patronus(self):
        return self._patronus

    def __str__(self):
        return "\n \
        \tVarita: {}.\n \
        \tPatronus: {}\n".format(self.varita, self.patronus)

class Mago():
    TUPLASANGRE=("Pura", "Mestiza", "Nacidos de Muggles", "Otra")
    ID=0

    def __init__(self, pNombre, pSangre, pEspecie, pMagias) -> None:
        self._id=Mago.ID
        Mago.ID+=1
        self._nombreCompleto=pNombre
        self._sangre=pSangre
        self._especie=pEspecie
        self._magias=pMagias

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, pId):
        self._id = pId

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
        return "Nombre: {} (Sangre: {}. Especie: {})\n\tMagias: {}".format(self.nombreCompleto, self.sangre, self.especie, self._magias)

    def prepararDict(self):
        dictPrep=self.__dict__.copy()
        dictPrep["_magias"]=self._magias.__dict__
        return dictPrep

    @staticmethod
    def setID(maxID):
        Mago.ID=maxID+1

def guardarJSONunMago(rutaFich, uno):
    with open(rutaFich, 'w') as f:
        json.dump(uno, f, indent=2)

def guardarJSONunMagoV2(rutaFich, uno: Mago):
    with open(rutaFich, 'w') as f:
        json.dump(uno.prepararDict(), f, indent=2)

def guardarJSONcoleccionMagos(rutaFich, coleccion):
    colAux=list()
    [colAux.append(c.prepararDict()) for c in coleccion] #Looping Using List 
    with open(rutaFich, 'w') as f:
        json.dump(colAux, f, indent=2)

def leerJSONyCargar(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)

    listaAux=list()
    max=0
    for i in cadjson:
        mag=Mago(i["_nombreCompleto"], i["_sangre"], i["_especie"],Magias(i["_magias"]["_varita"],i["_magias"]["_patronus"]))
        mag.id=i["_id"]
        listaAux.append(mag)
        if(max<mag.id):
            max=mag.id
    Mago.setID(max)
    return listaAux

def guardarJSONcoleccionMagosV2(rutaFich, coleccion):
    dictAux=dict()
    for c in coleccion:
        dictAux[c.id]=c.prepararDict()
    with open(rutaFich, 'w') as f:
        json.dump(dictAux, f, indent=2)

""" Pruebas """
if __name__ == "__main__":

    minerva = Mago("Minerva McGonagall", 1, "Humana", Magias("Abeto y fibra de corazón de dragón,", "Gato"))
    herminone = Mago("Hermione Granger", 2,"Humana", Magias("Vid y fibra de corazón de dragón", "Nutria"))

    listaMagos=[minerva,herminone]

    #guardarJSONunMago("ficheroUnMagoInter1.json", minerva)
    #guardarJSONunMago("ficheroUnMagoInter1.json", minerva.__dict__)
    guardarJSONunMagoV2("ficheroUnMagoInter1.json", minerva)

    guardarJSONcoleccionMagos("ficheroMagosInter1.json", listaMagos)

    del listaMagos
    del minerva
    del herminone

    listaMagos=leerJSONyCargar("ficheroMagosInter1.json")
    [print (m) for m in listaMagos]

    guardarJSONcoleccionMagosV2("ficheroMagosInter2.json", listaMagos)
