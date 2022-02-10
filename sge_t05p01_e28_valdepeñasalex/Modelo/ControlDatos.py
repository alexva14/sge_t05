import json
from Modelo.ClubModelo import Club
class ControlDatos:
    def __init__(self) -> None:
        pass

    def prepararDictSocio(c):
        dictPrep=c.__dict__.copy()
        dictPrep["_usuarioAsociado"]=c._usuarioAsociado._dni
        listaUsuariosAux=list()
        try:

            for i in dictPrep["bicicletas"]:
                lista=[]
                try:
                    for e in i._listaReparaciones:
                        lista.append(e.__dict__)
                        i.__dict__["_listaReparaciones"]=lista
                except:
                    continue
                listaUsuariosAux.append(i.__dict__)
                
                dictPrep["bicicletas"]=listaUsuariosAux
        except:
            dictPrep["bicicletas"]=listaUsuariosAux
        return dictPrep

    def prepararDictClub(c):
        dictPrep=c.copy()
        dictPrep["_dicSocios"]={}
        dictPrep["_listaEventos"]=[]
        dictPrep["_diccUsuarios"]={}
        
        return dictPrep

    def guardarDatos(club):
        #USUARIOS
        listaUsuariosAux=list()
        for i in club._diccUsuarios.values():
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONUsuarios("sge_t05p01_e28_valdepeñasalex/usuarios.json", listaUsuariosAux)
        del listaUsuariosAux

        #SOCIOS
        listaUsuariosAux=list()
        for e in club._dicSocios.values():
            socio=e
            listaUsuariosAux.append(socio)       

        colAux=list()
        for c in listaUsuariosAux:
            colAux.append(ControlDatos.prepararDictSocio(c)) #Looping Using List 
        Club.guardarJSONSocios("sge_t05p01_e28_valdepeñasalex/socios.json", colAux)

        #CLUB
        colAux=list()
        colAux.append(ControlDatos.prepararDictClub(club.__dict__))

        Club.guardarJSONClub("sge_t05p01_e28_valdepeñasalex/club.json", colAux )
        
        #EVENTOS
        listaUsuariosAux=list()
        for i in club._listaEventos:
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONEventos("sge_t05p01_e28_valdepeñasalex/eventos.json", listaUsuariosAux)
        del listaUsuariosAux
