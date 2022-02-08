from Modelo.SociosModelo import Socio
from Modelo.EventosModelo import Evento
from Modelo.UsuarioModelo import Usuario
import json
class Club:
    def __init__(self, nombreClub, cif, sedeSocial=None, saldoTotal=0, controlCuotas={}):
        self._nombreClub=nombreClub
        self._cif=cif
        self._sedeSocial=sedeSocial
        self._dicSocios={}
        self._listaEventos=[]
        self._saldoTotal=saldoTotal
        self._controlCuotas=controlCuotas
        self._diccUsuarios= {}
    
    def asignarListaSocios(self, diccionariosSocios):
            self._dicSocios=diccionariosSocios
        
    def asignarListaUsuarios(self, diccionarioUsuarios):
        self._diccUsuarios=diccionarioUsuarios
    
    def getUsuario(self, dni):
        return self._diccUsuarios[dni]

    def  getSocio(self, dni):
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

    ##ACCIONES CON EL JSON
    
    def guardarJSONUsuarios(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def leerJSONUsuarios(self):
        with open("sge_t05p01_e28_valdepeñasalex/usuarios.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            self._diccUsuarios[i["_dni"]]=(Usuario(i["_dni"], i["_contrasenna"], i["_ultimoAcceso"], i["_es_admin"], i["_corriente_pago"]))

    def leerJSONSocios(self):
        with open("sge_t05p01_e28_valdepeñasalex/socios.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            self._dicSocios[i["_usuarioAsociado"]]=(Socio(self.getUsuario(i["_usuarioAsociado"]), i["_nombreCompleto"], i["_direccion"], i["_telefono"], i["_correoElectronico"],  i["bicicletas"], i["familia"]))

    def leerJSONEventos(self):
        with open("sge_t05p01_e28_valdepeñasalex/eventos.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            self._listaEventos.append(Evento(i["_fechaEvento"],i["_fechaMaxInscripcion"],i["_localidad"],i["_provincia"],i["_organizador"],i["_kmTotales"],i["_precio"],i["_listadoSociosApuntados"]))
    
    def guardarJSONSocios(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def guardarJSONClub(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def guardarJSONEventos(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    