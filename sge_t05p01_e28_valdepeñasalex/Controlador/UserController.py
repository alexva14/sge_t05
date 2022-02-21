from Vista.VistaUser import VistaUser
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from datetime import datetime
from datetime import date
from Modelo.ControlDatos import ControlDatos
from Modelo.BicicletaModelo import Bicicleta
from Modelo.ReparacionModelo import Reparacion
from Modelo.CategoriasEnum import Categoria


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
            fecha=self._club._diccUsuarios[usuario]._ultimoAcceso
            while True:
                self._vista.mostrarMenu(usuario, fecha)
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")

    def controlOpciones(self,opc, usuario):
        if (opc == 0):
            #GUARDAR LA ULTIMA HORA DE ACCESO
            self._club._diccUsuarios[usuario]._ultimoAcceso=datetime.today().strftime('%d/%m/%Y')
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
        elif (opc == 5):
            self._vista.pedirDatosBicicleta(usuario)
        elif (opc == 6):
            listado = self.obtenerBicicletas(usuario)
            self._vista.verApuntarReparacion(listado, usuario)
        elif (opc == 7):
            familia = self._club._dicSocios[usuario].familia
            self._vista.mostarFamilia(familia)
        elif (opc == 8):
            cuotas = self.obtenerDatosCuotas(usuario)
            self._vista.mostrarDatosCuotas(cuotas)
    
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
            #for e in i._listaReparaciones:
            listadoReparaciones.append(i)
        return listadoReparaciones

    def agregarBicicleta(self, fecha, marca, modelo, tipo, color, cuadro, ruedas, precio, usuario):
        self._club._dicSocios[usuario].bicicletas.append(Bicicleta(fecha,marca, modelo, tipo, color, cuadro, ruedas, precio, []))
    
    def crearReparacionBicicleta(self, e, usuario, listado, fecha, coste, descripcion, categoria):
        listado[e]._listaReparaciones.append(Reparacion(fecha, coste, descripcion, categoria))
    
    def obtenerSocio(self, dni):
        return self._club._dicSocios[dni]
    
    def obtenerDatosCuotas(self, usuario):
        cuotas={}
        for i in self._club._controlCuotas:
            for e in self._club._controlCuotas[i]:
                if e==usuario:
                    cuotas[i]=self._club._controlCuotas[i][e]
        return cuotas
                    
    def comprobarCategoria(self, categoria):
        try:
            for c in Categoria:
                if c.name==categoria:
                    return False
            return True
        except:
            return True