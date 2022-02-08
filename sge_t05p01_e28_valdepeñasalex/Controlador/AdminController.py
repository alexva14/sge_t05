from datetime import datetime, time

from Vista.VistaAdmin import VistaAdmin
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from Modelo.SociosModelo import Socio
from Modelo.UsuarioModelo import Usuario
from Modelo.EventosModelo import Evento


class ControladorAdmin:

    def __init__(self,  club: Club, usuario, contrasenna):
        self._club=club
        self._vista=VistaAdmin(self)
        self.inicio(usuario, contrasenna)

    def inicio(self, usuario, contrasenna):
        #Prueba.cargarUsuarios(self._club)
        Club.leerJSONUsuarios(self._club)
        #Prueba.cargarSocios(self._club)
        Club.leerJSONSocios(self._club)
        #Prueba.cargarControlCuotas(self._club)
        Club.leerJSONEventos(self._club)
        #Prueba.cargarEventos(self._club)
        resultado=self._club.verificarUsuariosAdm(usuario, contrasenna)
        if(resultado==1):
            while True:
                self._vista.mostrarMenu(usuario)
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")
    

    def prepararDictSocio(self,c):
        dictPrep=c.__dict__.copy()
        dictPrep["_usuarioAsociado"]=c._usuarioAsociado._dni
        return dictPrep

    def prepararDictClub(self,c):
        dictPrep=c.copy()
        dictPrep["_dicSocios"]={}
        dictPrep["_listaEventos"]=[]
        dictPrep["_diccUsuarios"]={}
        
        return dictPrep

    def guardarDatos(self):
        #USUARIOS
        listaUsuariosAux=list()
        for i in self._club._diccUsuarios.values():
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONUsuarios("sge_t05p01_e28_valdepeñasalex/usuarios.json", listaUsuariosAux)
        del listaUsuariosAux

        #SOCIOS
        listaUsuariosAux=list()
        for e in self._club._dicSocios.values():
            socio=e
            listaUsuariosAux.append(socio)       

        colAux=list()
        for c in listaUsuariosAux:
            colAux.append(self.prepararDictSocio(c)) #Looping Using List 
        Club.guardarJSONSocios("sge_t05p01_e28_valdepeñasalex/socios.json", colAux)

        #CLUB
        colAux=list()
        colAux.append(self.prepararDictClub(self._club.__dict__))

        Club.guardarJSONClub("sge_t05p01_e28_valdepeñasalex/club.json", colAux )
        
        #EVENTOS
        listaUsuariosAux=list()
        for i in self._club._listaEventos:
            listaUsuariosAux.append(i.__dict__)
        
        Club.guardarJSONEventos("sge_t05p01_e28_valdepeñasalex/eventos.json", listaUsuariosAux)
        del listaUsuariosAux


    def ControlOpciones(self, opc):
        if (opc == 0):
            self.guardarDatos()
            self._vista.salir()
        elif (opc == 1):
            lista=self.sacarListaSocios()
            self._vista.mostrarSocios(lista)
        elif (opc == 2):
            self._vista.pedirDatosSocio()
        elif (opc ==3):
            self._vista.pedirDatosFamiliar()
        elif (opc ==4):
            lista=self.sacarListaEventosProximos()
            self._vista.mostrarEventos(lista)
        elif (opc ==5):
            self._vista.pedirFecha()
        elif (opc ==6):
            self._vista.pedirDatosEventos()
        elif (opc ==7):
            año=self._vista.pedirAñoControlCuotas()
            cuotas=self.sacarCuotas(str(año))
            self._vista.mostrarControlCuotas(cuotas, self._club)
        elif (opc ==8):
            existe=self.comprobarControlCuotas()
            if existe:
                self._vista.mostrarMensaje("El control de cuotas de este año ya estaba creado")
            else:
                self.crearControlCuotasAño()
                self._vista.mostrarMensaje("El control de cuotas del año en curso ha sido creado con los datos nuevos")
        elif (opc ==9):
            self._vista.pedirPagarCuota()
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
        (self._club._controlCuotas["2022"])[dni]=[2022, dni, self._club.getUsuario(dni)._corriente_pago, 15, 0, datetime.today().strftime('%Y/%m/%d')]

    def añadirFamiliares(self, opc, dni):
        if (opc == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if(self._club._dicSocios[dni].familia["Pareja"]==None and len(self._club._dicSocios[dni].familia["Padres"])==0):
                self._vista.pedirDatosPareja(dni)
            else:
                return 1
        elif (opc == 2):
            if ( self._club._dicSocios[dni].familia["Pareja"]==None): return 2
            
            elif(len(self._club._dicSocios[dni].familia["Hijos"])<=1  and len(self._club._dicSocios[dni].familia["Padres"])==0):
                self._vista.pedirDatosHijo(dni)
            else: return 3
        elif (opc ==3):
            if (self._club._dicSocios[dni].familia["Pareja"]==None and len(self._club._dicSocios[dni].familia["Padres"])==0):
                self._vista.pedirDatosPadres(dni)
            else:
                return 4
    
    def añadirPareja(self, dnipareja1, dnipareja2):
        #buscamos a la pareja 1 y le asignamos la pareja2
        self._club._dicSocios[dnipareja1].familia["Pareja"]=dnipareja2
        self._club._dicSocios[dnipareja2].familia["Pareja"]=dnipareja1
        
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
        self.actualizarcuotasañadirHijos(dnipareja1, dnipareja2, dnihijo)
    
    def añadirPadres(self, dnihijo, dnipareja1):
        #busco la pareja del padre
        dnipareja2=self._club._dicSocios[dnipareja1].familia["Pareja"]._usuarioAsociado._dni
        #le asignamos el hijo a ambos miembros de la pareja
        self._club._dicSocios[dnipareja1].familia["Hijos"].append(self._club._dicSocios[dnihijo])
        self._club._dicSocios[dnipareja2].familia["Hijos"].append(self._club._dicSocios[dnihijo])
        #buscamos al hijo y le asignamos los padres
        self._club._dicSocios[dnihijo].familia["Padres"]=(self._club._dicSocios[dnipareja1], self._club._dicSocios[dnipareja2])
        self.actualizarcuotasañadirHijos(dnipareja1, dnipareja2, dnihijo)

    def comprobarPadres(self, dnihijo):
        if (len(self._club._dicSocios[dnihijo].familia["Padres"])==0):return False
        else: return True
    
    def comprobarPareja(self, dni):
        if (self._club._dicSocios[dni].familia["Pareja"]==None):return True
        else: return False

    def comprobarHijos(self, dni):
        if (len(self._club._dicSocios[dni].familia["Hijos"])<=1):return False
        else:return True
    

    def actualizarcuotasañadirPareja(self, dnipareja1, dnipareja2):
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][4]=10
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][3]=15*0.9
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja2][4]=10
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja2][3]=15*0.9
    
    def actualizarcuotasañadirHijos(self, dnipareja1, dnipareja2, dnihijo):
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][3]=15*0.7 
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja2][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja2][3]=15*0.7
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][3]=15*0.7
    
    def sacarListaEventosProximos(self):
        lista=[]
        for i in self._club._listaEventos:
            fecha=datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                lista.append(i)
        return lista

    def buscarEvento(self, fecha):
        lista=[]
        for i in self._club._listaEventos:
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))==(datetime.strptime(fecha,'%d/%m/%Y')):
                lista.append(i)
        return lista
    
    def crearEvento(self, fecha_inicio, fecha_ins, lugar, provincia, organizacion, distancia, precio, socios):
        self._club._listaEventos.append(Evento(fecha_inicio, fecha_ins, lugar, provincia, organizacion, distancia, precio, socios))
    
    def sacarCuotas(self,año):
        try:
            return self._club._controlCuotas[año]
        except:
            return ""
    
    def comprobarControlCuotas(self):
        year = str(datetime.today().strftime('%Y'))
        try:
            datos=self._club._controlCuotas[year]
            return True
        except:
            return False
    
    def crearControlCuotasAño(self):
        year = int(datetime.today().strftime('%Y'))
        controlcuotas=self._club._controlCuotas[str(year-1)]
        self._club._controlCuotas[str(year)]=controlcuotas
        #ahora lo recorremos y ponemos a todos los usuarios que no han pagado
        for dni in self._club._controlCuotas[str(year)]:
            self._club._controlCuotas[str(year)][dni][2]=False

    def comprobarPagado(self,dni):
        year = str(datetime.today().strftime('%Y'))
        if self._club._controlCuotas[year][dni][2]:
            return True
        else: return False
    
    def obtenerCantidadPagar(self,dni):
        year = str(datetime.today().strftime('%Y'))
        return self._club._controlCuotas[year][dni][3] 
    
    def pagarCuota(self,dni):
        year = str(datetime.today().strftime('%Y'))
        self._club.getUsuario(dni)._corriente_pago=True
        self._club._controlCuotas[year][dni][2]= self._club.getUsuario(dni)._corriente_pago

