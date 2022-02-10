from Vista.VistaUser import VistaUser
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from datetime import datetime
from datetime import date
from Modelo.ControlDatos import ControlDatos

class ControladorUser:
    def __init__(self,  club: Club, usuario, contrasenna):
        self._club=club
        self._vista=VistaUser(self)
        self.inicio(usuario, contrasenna)
        

    def inicio(self, usuario, contrasenna):
        #Prueba.cargarUsuarios(self._club)
        Club.leerJSONUsuarios(self._club)
        #Prueba.cargarSocios(self._club)
        Club.leerJSONSocios(self._club)
        #Prueba.cargarControlCuotas(self._club)
        Club.leerJSONEventos(self._club)

        resultado=self._club.verificarUsuariosUs(usuario, contrasenna)

        if(resultado==1):
            while True:
                self._vista.mostrarMenu(usuario)
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")

    def controlOpciones(self,opc, usuario):
        if (opc == 0):
            ControlDatos.guardarDatos(self._club)
            self._vista.salir()
        elif (opc == 1):
            listado = self.obtenerEventosUsuario(usuario)
            self._vista.mostrarMisProxEventos(listado)
        elif (opc == 2):
            listado = self.obtenerEventosParaTodos()
            self._vista.verApuntarEvento(listado, usuario)
        elif (opc == 3):
            listado = self.obtenerBicicletas(usuario)
            self._vista.mostrarBicicletas(listado)
        elif (opc == 4):
            listado = self.obtenerReparaciones(usuario)
            self._vista.mostrarReparaciones(listado)
    
    def obtenerEventosUsuario(self, usuario):
        listado = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                for j in i._listadoSociosApuntados:
                    if(j==usuario):
                        listado.append(i)
        return listado

    def obtenerEventosParaTodos(self):
        listado = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                listado.append(i)
        return listado

    def controlarSocioEvento(self, usuario, e, listado):
        apuntado=False
        for i in listado[e]._listadoSociosApuntados:
            if i==usuario:
                apuntado=True
        return apuntado

    def apuntarSocioEvento(self, usuario, posicion, eventosfuturos):
        eventosfuturos[posicion]._listadoSociosApuntados.append(usuario)
        #saco la lista de los eventos que son antiguos
        eventospasados = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))<(datetime.today().strptime(fecha, '%d/%m/%Y')):
                eventospasados.append(i)
        #añado los eventos pasados a una nueva lista
        eventos=[]
        for i in eventospasados:
            eventos.append(i)
        for i in eventosfuturos:
            eventos.append(i)
        self._club._listaEventos=eventos

        
    def obtenerBicicletas(self, usuario):
        listadoBicicletas = []
        for i in self._club._dicSocios[usuario].bicicletas:
            listadoBicicletas.append(i)
        return listadoBicicletas
    
    def obtenerReparaciones(self, usuario):
        listadoReparaciones = []
        for i in self._club._dicSocios[usuario].bicicletas:
            for e in i._listaReparaciones:
                listadoReparaciones.append(e)
        return listadoReparaciones
