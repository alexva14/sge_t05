import json
from Modelo.ClubModelo import Club

class ControlDatos:
    def guardarDatos(self, club):
        #USUARIOS
        listaUsuariosAux=list()
        for i in self._club._diccUsuarios.values():
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONUsuarios("usuarios.json", listaUsuariosAux)
        del listaUsuariosAux

        #SOCIOS
        listaUsuariosAux=list()
        for e in self._club._dicSocios.values():
            socio=e
            listaUsuariosAux.append(socio)       

        colAux=list()
        for c in listaUsuariosAux:
            colAux.append(self.prepararDictSocio(c)) #Looping Using List 
        Club.guardarJSONSocios("socios.json", colAux)

        #CLUB
        colAux=list()
        colAux.append(self.prepararDictClub(self._club.__dict__))

        Club.guardarJSONClub("club.json", colAux )
        
        #EVENTOS
        listaUsuariosAux=list()
        for i in self._club._listaEventos:
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONEventos("eventos.json", listaUsuariosAux)
        del listaUsuariosAux
