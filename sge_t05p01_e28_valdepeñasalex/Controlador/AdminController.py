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
        Prueba.cargarControlCuotas(self._club)
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

    def sacarListaSocios(self):#echar un ojo ya que recorremos dos veces
        lista=[]
        for clave in self._club._dicSocios:
            valor = self._club._dicSocios[clave] 
            lista.append(valor._nombreCompleto)
        return lista

    def comprobarExisteDni(self, dni):#mirar
        for clave in self._club._dicSocios:
            if clave==dni:
                return False
        return True

    def crearSocUser(self, dni, contrasenna, admin, nombre, direccion, telefono, correo):
        #creamos el usuario
        self._club._diccUsuarios[dni]=Usuario (dni, contrasenna, datetime.today().strftime('%Y/%m/%d'), admin, True)
        #añadimos el nuevo socio
        self._club._dicSocios[dni]= Socio (self._club.getUsuario(dni), nombre, direccion, telefono, correo)
        #añadimos al control de cutoas
        self.añadirUserControlCuotas(dni)

    def añadirUserControlCuotas(self,dni):
        (self._club._controlCuotas[2022])[dni]=(2022, self._club.getSocio(dni), self._club.getUsuario(dni)._corriente_pago, 15, 0, datetime.today().strftime('%Y/%m/%d'))

    def añadirFamiliares(self, opc, dni):
        if (opc == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if(self._club._dicSocios[dni].familia["Pareja"]==None and self._club._dicSocios[dni].familia["Padres"]==None ):
                self._vista.pedirDatosPareja(dni)
            else:
                return 1
        elif (opc == 2):
            if ( self._club._dicSocios[dni].familia["Pareja"]==None): return 2
            
            elif(len(self._club._dicSocios[dni].familia["Hijos"])<=1  and self._club._dicSocios[dni].familia["Padres"]==None ):
                self._vista.pedirDatosHijo(dni)
            else: return 3
        elif (opc ==3):
            if (self._club._dicSocios[dni].familia["Pareja"]==None):
                self._vista.pedirDatosPadres(dni)
    
    def añadirPareja(self, dnipareja1, dnipareja2):
        #buscamos a la pareja 1 y le asignamos la pareja2
        self._club._dicSocios[dnipareja1].familia["Pareja"]=self._club._dicSocios[dnipareja2]
        self._club._dicSocios[dnipareja2].familia["Pareja"]=self._club._dicSocios[dnipareja1]
        
        #ahora vamos a actualizar las cuotas
        self.actualizarcuotasañadirPareja(dnipareja1, dnipareja2)
        
    def añadirHijo(self, dnipareja1, dnihijo):
        #buscamos la pareja y le asignamos el hijo
        self._club._dicSocios[dnipareja1].familia["Hijos"].append(self._club._dicSocios[dnihijo])
        #sacamos la pareja del padre
        dnipareja2=self._club._dicSocios[dnipareja1].familia["Pareja"]._usuarioAsociado._dni
        self._club._dicSocios[dnipareja2].familia["Hijos"].append(self._club._dicSocios[dnihijo])

        #buscamos al hijo y le asignamos los padres
        self._club._dicSocios[dnihijo].familia["Padres"]=(self._club._dicSocios[dnipareja1], self._club._dicSocios[dnipareja2])
    
    def comprobarPadres(self, dnihijo):
        if (self._club._dicSocios[dnihijo].familia["Padres"]==None):return False
        else: return True

    def actualizarcuotasañadirPareja(self, dnipareja1, dnipareja2):
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][4]=10
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][3]=self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][4]*0,9
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][4]=10
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][3]=self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][4]*0,9
    
    def actualizarcuotasañadirHijos(self, dnipareja1, dnipareja2, dnihijo):
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][4]=30
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][3]=self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja1][4]*0,7 
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][4]=30
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][3]=self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][4]*0,7
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnihijo][4]=30
        self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnihijo][3]=self._club._controlCuotas[int(datetime.today().strftime('%Y'))][dnipareja2][4]*0,7