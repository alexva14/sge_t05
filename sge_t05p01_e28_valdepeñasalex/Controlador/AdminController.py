from asyncio import run_coroutine_threadsafe
from datetime import datetime, time

from Vista.VistaAdmin import VistaAdmin
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from Modelo.SociosModelo import Socio
from Modelo.UsuarioModelo import Usuario
from Modelo.EventosModelo import Evento
from Modelo.ControlDatos import ControlDatos



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
        #resultado=self.verificarAcceso(usuario, contrasenna)
        if(resultado==1):
            fecha=self._club._diccUsuarios[usuario]._ultimoAcceso
            while True:
                self._vista.mostrarMenu(usuario, fecha)
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        elif(resultado==3):
            self._vista.mostrarError("Han pasado mas de 30 días de tu acceso y no habias pagado la cuota. Ponte en contacto con un administrador para pagarla")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")
    
    def verificarAcceso(self, usuario, contrasenna):
        today=datetime.strptime( datetime.today().strftime('%d/%m/%Y') ,"%d/%m/%Y")
        ult_acceso=datetime.strptime(self._club._diccUsuarios[usuario]._ultimoAcceso, "%d/%m/%Y")
        diferencia = today-ult_acceso
        if diferencia.days>30:
            if(self._club._diccUsuarios[usuario]._corriente_pago):
                return 1
            else: return 3
        else:
            return 1

    def ControlOpciones(self, opc, usuario):
        if (opc == 0):
            self._club._diccUsuarios[usuario]._ultimoAcceso=datetime.today().strftime('%d/%m/%Y')
            ControlDatos.guardarDatos(self._club)
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
        self._club._diccUsuarios[dni]=Usuario (dni, contrasenna, datetime.today().strftime('%d/%m/%Y'), admin, True)
        #añadimos el nuevo socio
        self._club._dicSocios[dni]= Socio (self._club.getUsuario(dni), nombre, direccion, telefono, correo)
        #añadimos al control de cutoas
        self.añadirUserControlCuotas(dni)

    def añadirUserControlCuotas(self,dni):
        year = datetime.today().strftime('%Y')
        mes= int(datetime.today().strftime('%m'))
        if mes<7:
            (self._club._controlCuotas[str(year)])[dni]=[int(year), dni, self._club.getUsuario(dni)._corriente_pago, 15, 0, datetime.today().strftime('%Y/%m/%d')]
        else:
            (self._club._controlCuotas[str(year)])[dni]=[int(year), dni, self._club.getUsuario(dni)._corriente_pago, 8, 0, datetime.today().strftime('%Y/%m/%d')]


    def añadirFamiliares(self, opc, dni):
        if (opc == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if(self._club._dicSocios[dni].familia["Pareja"]==None and len(self._club._dicSocios[dni].familia["Padres"])==0):
                self._vista.pedirDatosPareja(dni)
            else:
                return 1
        elif (opc == 2):
            if(len(self._club._dicSocios[dni].familia["Padres"])==0):
                self._vista.pedirDatosHijo(dni)
            else: return 3
        elif (opc ==3):
            if (self._club._dicSocios[dni].familia["Pareja"]==None and len(self._club._dicSocios[dni].familia["Padres"])<2):
                self._vista.pedirDatosPadres(dni)
            else:
                return 4
    
    def añadirPareja(self, dnipareja1, dnipareja2):
        #buscamos a la pareja 1 y le asignamos la pareja2
        self._club._dicSocios[dnipareja1].familia["Pareja"]=dnipareja2
        self._club._dicSocios[dnipareja2].familia["Pareja"]=dnipareja1

        #comprobamos si pareja1 tiene hijos
        if (len(self._club._dicSocios[dnipareja1].familia["Hijos"])>0):
            #le asignamos los hijos de pareja1 a pareja2
            for i in self._club._dicSocios[dnipareja1].familia["Hijos"]:
                self._club._dicSocios[dnipareja2].familia["Hijos"].append(i)
            #actualizamos las cuotas
            lista=[dnipareja1, dnipareja2]
            for i in self._club._dicSocios[dnipareja1].familia["Hijos"]:
                self._club._dicSocios[i].familia["Padres"]=[]
                self._club._dicSocios[i].familia["Padres"].append(dnipareja2)
                lista.append(i)
            self.actualizarCuotasPadresHijos(lista)

        #comprobamos si pareja2 tiene hijos
        if (len(self._club._dicSocios[dnipareja2].familia["Hijos"])>0):
            #le asignamos los hijos de pareja1 a pareja2
            self._club._dicSocios[dnipareja1].familia["Hijos"]=self._club._dicSocios[dnipareja2].familia["Hijos"]
            lista=[dnipareja1, dnipareja2]
            for i in self._club._dicSocios[dnipareja2].familia["Hijos"]:
                #self._club._dicSocios[i].familia["Padres"]=[]
                self._club._dicSocios[i].familia["Padres"].append(dnipareja1)
                lista.append(i)
            self.actualizarCuotasPadresHijos(lista)
        else:
            #ahora vamos a actualizar las cuotas
            self.actualizarcuotasañadirPareja(dnipareja1, dnipareja2)
    
    def actualizarCuotasPadresHijos(self, lista):
        for i in lista:
            self._club._controlCuotas[str(datetime.today().strftime('%Y'))][i][4]=30
            self._club._controlCuotas[str(datetime.today().strftime('%Y'))][i][3]=15*0.7

    def añadirHijo(self, dnipareja1, dnihijo):
        #buscamos la pareja y le asignamos el hijo
        self._club._dicSocios[dnipareja1].familia["Hijos"].append(dnihijo)
        #sacamos la pareja del padre
        try:
            dnipareja2=self._club.getSocio(self._club._dicSocios[dnipareja1].familia["Pareja"])._usuarioAsociado._dni
            self._club._dicSocios[dnipareja2].familia["Hijos"].append(dnihijo)
            #buscamos al hijo y le asignamos los padres
            self._club._dicSocios[dnihijo].familia["Padres"]=[dnipareja1, dnipareja2]
            self.actualizarcuotasañadirHijos(dnipareja1, dnipareja2, dnihijo)
            
        except:
            #buscamos al hijo y le asignamos el padre
            self._club._dicSocios[dnihijo].familia["Padres"]=[dnipareja1]
            self.actualizarcuotasañadirHijo(dnipareja1, dnihijo)

    def comprobarPadre(self, dnipareja2, dniuser):
        if (len(self._club._dicSocios[dniuser].familia["Padres"])==1 and self._club._dicSocios[dnipareja2].familia["Pareja"]!= None):
            return True
        else:
            return False
    
    def añadirPadres(self, dnihijo, dnipareja1):
        #busco la pareja del padre
        try:
            dnipareja2=self._club.getSocio(self._club._dicSocios[dnipareja1].familia["Pareja"])._usuarioAsociado._dni
            #le asignamos el hijo a ambos miembros de la pareja
            self._club._dicSocios[dnipareja1].familia["Hijos"].append(dnihijo)
            self._club._dicSocios[dnipareja2].familia["Hijos"].append(dnihijo)
            #buscamos al hijo y le asignamos los padres
            self._club._dicSocios[dnihijo].familia["Padres"]=(dnipareja1, dnipareja2)
            self.actualizarcuotasañadirHijos(dnipareja1, dnipareja2, dnihijo)
        except:
            self._club._dicSocios[dnipareja1].familia["Hijos"].append(dnihijo)
            self._club._dicSocios[dnihijo].familia["Padres"].append(dnipareja1)
            self.actualizarcuotasañadirHijo(dnipareja1, dnihijo)

        

    def comprobarPadres(self, dnihijo):
        if (len(self._club._dicSocios[dnihijo].familia["Padres"])<2):return False
        else: return True
    
    def comprobarPareja(self, dni):
        if (self._club._dicSocios[dni].familia["Pareja"]==None):return True
        else: return False

    def comprobarHijos(self, dni):
        if (len(self._club._dicSocios[dni].familia["Hijos"])<=1):return False
        else:return True
    
    def sacarDniPareja(self, dnipareja1):
        return self._club._dicSocios[dnipareja1].familia["Pareja"]

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
    
    def actualizarcuotasañadirHijo(self, dnipareja1, dnihijo):
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][4]=15
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnipareja1][3]=15*0.85
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][4]=15
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][3]=15*0.85

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
            self._club._controlCuotas[str(year)][dni][3]=15*(100-self._club._controlCuotas[str(year)][dni][4])/100
            self._club._controlCuotas[str(year)][dni][5]=""
        #recorro la lista de usuarios y pongo su corriente de pago a false
        for i in self._club._diccUsuarios:
            self._club._diccUsuarios[i]._corriente_pago=False

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
        #ACTAULIZAMOS LA FECHA DE PAGO A LA ACTUAL
        self._club._controlCuotas[year][dni][5]=datetime.today().strftime('%d/%m/%Y')
