from datetime import datetime


from datetime import datetime

from Vista.VistaAdmin import VistaAdmin
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from Modelo.SociosModelo import Socio
from Modelo.UsuarioModelo import Usuario


class ControladorAdmin:

    def __init__(self,  club: Club, usuario, contrasenna):
        self._club=club
        self._vista=VistaAdmin(self)
        self.inicio(usuario, contrasenna)

    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        resultado=self._club.verificarUsuariosAdm(usuario, contrasenna)
        if(resultado==1):
            while True:
                self._vista.mostrarMenu(usuario)
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")
    
    def ControlOpciones(self, opc):
        if (opc == 0): 
            self._vista.salir()
        elif (opc == 1):
            lista=self.sacarListaSocios()
            self._vista.mostrarSocios(lista)
        elif (opc == 2):
            datos=self._vista.pedirDatosSocio()
        elif (opc ==3):
            self._vista.pedirDatosFamiliar()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def sacarListaSocios(self):
        lista=[]
        for clave in self._club._dicSocios:
            valor = self._club._dicSocios[clave] 
            lista.append(valor._nombreCompleto)
        return lista

    def comprobarExisteDni(self, dni):
        for clave in self._club._dicSocios:
            if clave==dni:
                return False
        return True

    def crearSocUser(self, dni, contrasenna, admin, nombre, direccion, telefono, correo):
        #creamos el usuario
        self._club._diccUsuarios[dni]=Usuario (dni, contrasenna, datetime.today().strftime('%Y/%m/%d'), admin)
        #añadimos el nuevo socio
        self._club._dicSocios[dni]= Socio (self._club.getUsuario(dni), nombre, direccion, telefono, correo)

    def añadirFamiliares(self, opc, dni):
        if (opc == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if(self._club._dicSocios[dni].familia["Pareja"]==None):
                self._vista.pedirDatosPareja(dni)
            else:
                return 1
        elif (opc == 2):
            datos=self._vista.pedirDatosSocio()
        else:
            datos
