from Modelo.SociosModelo import Socio
from Modelo.EventosModelo import Evento
from Modelo.UsuarioModelo import Usuario

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

    def getSocio(self, dni):
        return self._dicSocios[dni]
    
    def verificarUsuarioAdmin(self, argumentos):
        if len(argumentos)==6:
            if argumentos[5]=="-A":return True                  
        if len(argumentos)==5:return False        

    def verificarUsuariosAdm(self, usuario: Usuario, contrasenna):
        try:
            if(self._diccUsuarios[usuario]):
                usuario=self._diccUsuarios[usuario]
                if(contrasenna==usuario._contrasenna):
                    if(usuario._es_admin):return 1
                    else:return 3                      
                else:return 2               
            else:return 2             
        except:return 2        

    def verificarUsuariosUs(self, usuario: Usuario, contrasenna):
        try:
            if(self._diccUsuarios[usuario]):
                usuario=self._diccUsuarios[usuario]
                if(contrasenna==usuario._contrasenna):
                    return 1
                else:return 2
            else:return 2
        except:return 2
            