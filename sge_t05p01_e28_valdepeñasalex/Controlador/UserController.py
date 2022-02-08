from Vista.VistaUser import VistaUser
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from datetime import datetime
from datetime import date

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

    #algo para el segundo apartado
    def apuntarSocioEvento(self, usuario, posicion):
        self._club._listaEventos[posicion]._listadoSociosApuntados.append(usuario)
        
    def obtenerBicicletas(self, usuario):
        listadoBicicletas = []
        for i in self._club._dicSocios[usuario]._bicicletas:
            listadoBicicletas.append(i)
        return listadoBicicletas
