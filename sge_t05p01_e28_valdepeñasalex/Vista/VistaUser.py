from datetime import date
from datetime import datetime


class VistaUser:

    def __init__(self, contr): 
        self._controlador=contr

    def inicio(self):
        fdate = date.today().strftime('%d/%m/%Y')
        print("Bienvenido. Hoy es: {}".format(fdate))
        self.mostrarMenu()
        try:
            opc=self.leerOpcionMenu()
            #self._controlador.controlOpciones(opc)
        except Exception as exc:
                self.mostrarError(exc)
        finally:
                self.salir

    def mostrarMenu(self, usuario, fecha):
        print("")
        print("************************************************")
        print("*              LOS SATANASES DEL               *")
        print("*                INFIERNO APP                  *")
        print("************************************************")
        print("*             Zona de usuarios                 *")
        print("*                Usuario: ",usuario,"          *")
        print("*                Último acc.:",fecha,"      *")
        print("************************************************")
        print("")
        print("====")
        print("1. Ver mis próximos eventos y la lista de inscritos")
        print("2. Ver y apuntarme a eventos abiertos")
        print("3. Ver mis bicicletas")
        print("4. Ver mis reparaciones/mantenimientos")
        print("5. Añadir nueva bicicleta")
        print("6. Añadir reparación/mantenimiento a una de mis bicicletas")
        print("7. Ver mi familia")
        print("8. Ver mi histórico y estado de cuotas")
        print("0. Salir.")
        self.leerOpcionMenu(usuario)
    
    def leerOpcionMenu(self, usuario):
        try:
            opc=int(input("Deme una opción: "))
        except:
            opc=0
            print("Debes introducir un número entero. Se cerrara el programa")
        if (opc >=0 and opc <=8):
            self._controlador.controlOpciones(opc, usuario)
        else:
            print("Debes introducir un número entero entre 0 y 8.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")
        quit()
    
    def mostrarMisProxEventos(self, listado):
        if(len(listado)>0):
            print("Tus eventos para los próximos días son: ")
            for i in listado: 
                print("Fecha: ", i._fechaEvento)
                print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
                print("Localidad: ", i._localidad)
                print("Provincia: ", i._provincia)
                print("Organización: ", i._organizador)
                print("KM Totales: ", i._kmTotales)
                print("Precio: ", i._precio)
                print("Socios Apuntados: ")
                print("NOMBRE              TELEFONO  ")
                for j in i._listadoSociosApuntados:
                    socio=self._controlador.obtenerSocio(j)
                    print("{:<20} {:<9}".format(socio._nombreCompleto, socio._telefono))
                print("-------------------------------------")
        else: 
            print("No Tienes Eventos para los próximos días")
        print("Pulsa Intro para continuar...")
        input()

    def verApuntarEvento(self, listado, usuario):
        if(len(listado)>0):
            print("Los eventos disponibles actualmente son: ")
            e = 0
            while(len(listado)>0):
                if(e==len(listado)):
                    break
                for i in listado: 
                    print("Fecha: ", i._fechaEvento)
                    print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
                    print("Localidad: ", i._localidad)
                    print("Provincia: ", i._provincia)
                    print("Organización: ", i._organizador)
                    print("KM Totales: ", i._kmTotales)
                    print("Precio: ", i._precio)
                    print("¿Deseas apuntarte a este evento (si/no)?")
                    respuesta=input()
                    if(respuesta.lower()=="si"): 
                        if (self._controlador.controlarSocioEvento(usuario, e, listado)):
                            print("Ya estas apuntado a este evento")
                        else:
                                self._controlador.apuntarSocioEvento(usuario, e, listado)
                                print("Apuntado al evento con exito")
                        
                        respuesta=True
                    e+=1
        else:
            print("No hay eventos disponibles")
        print("Pulsa Intro para continuar...")
        input()


    def mostrarBicicletas(self, listado):
        if(len(listado)>0):
            print("Tus bicicletas son: ")
            for i in listado: 
                print("Fecha Compra: ", i._fechaCompra)
                print("Marca: ", i._marca)
                print("Modelo: ", i._modelo)
                print("Tipo: ", i._tipo)
                print("Color: ", i._color)
                print("Tamaño Cuadro: ", i._tamannoCuadro)
                print("Tamaño Ruedas: ", i._tamannoRuedas)
                print("Precio: ", i._precio)
                print("-------------------------------------")
        else: 
            print("No tienes bicicletas disponibles")
        print("Pulsa Intro para continuar...")
        input()
    
    def mostrarReparaciones(self, listado):
        if(len(listado)>0):
            print("Tus reparaciones/mantenimientos realizados a tus diferentes bicicletas son: ")
            print()
            for i in listado: 
                print("*****************************")
                print("Bicicleta: ",i._marca)
                print("*****************************")
                for e in i._listaReparaciones:
                    print("Fecha: ", e._fecha)
                    print("Coste: ", e._coste)
                    print("Descripción: ", e._descripcion)
                    print("Categoria: ", e._categoria)
                    print("-------------------------------------")
        else: 
            print("No tienes reparaciones realizadas")
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirDatosBicicleta(self, usuario):
        correcto= True
        while correcto:
            try:
                print("Introduce la fechade compra (dia/mes/año es decir **/**/****)")
                fecha=input()
                prueba=datetime.strptime(fecha,'%d/%m/%Y')
                correcto=False
            except:
                print("Introduce una fecha correcta")
        print("Introduce la marca de la bicicleta:")
        marca=input()
        print("Introduce el modelo de la bicicleta:")
        modelo=input()
        print("Introduce el tipo de bicicleta:")
        tipo=input()
        print("Introduceel color de la bicicleta:")
        color=input()
        print("Introduce las dimensiones del cuadro de la bicicleta:")
        cuadro=float(input())
        print("Introduce las dimensiones de las ruedas de la bicicleta:")
        ruedas=input()
        print("Introduce el precio de la bicicleta:")
        precio=input()
        self._controlador.agregarBicicleta(fecha, marca, modelo, tipo, color, cuadro, ruedas, precio, usuario)
        print("Bicicleeta agregada correctamente...")
        print("Pulsa Intro para continuar...")
        input()

    def verApuntarReparacion(self, listado, usuario):
        if(len(listado)>0):
            print("Los bicicletas disponibles actualmente son: ")
            e = 0
            while(len(listado)>0):
                if(e==len(listado)):
                    break
                for i in listado: 
                    print("Fecha Compra: ", i._fechaCompra)
                    print("Marca: ", i._marca)
                    print("Modelo: ", i._modelo)
                    print("Tipo: ", i._tipo)
                    print("Color: ", i._color)
                    print("Tamaño Cuadro: ", i._tamannoCuadro)
                    print("Tamaño Ruedas: ", i._tamannoRuedas)
                    print("Precio: ", i._precio)
                    print("¿Deseas añadir una reparación a esta bicicleta(si/no)?")
                    respuesta=input()
                    if(respuesta.lower()=="si"): 
                        self.pedirDatosReparacion(e, usuario, listado)
                    e+=1
        else:
            print("No hay bicicletas disponibles para añadirles reparaciones")
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirDatosReparacion(self,e, usuario, listado):
        correcto= True
        while correcto:
            try:
                print("Introduce la fecha de la reparación (dia/mes/año es decir **/**/****)")
                fecha=input()
                prueba=datetime.strptime(fecha,'%d/%m/%Y')
                correcto=False
            except:
                print("Introduce una fecha correcta")
        correcto= True
        while correcto:
            try:
                print("Introduce el coste de la reparación:")
                coste=float(input())
                correcto=False
            except:
                print("Introduce una cifra correcta")
        print("Introduce una breve descripción: ")
        descripcion=input()
        correcto=True
        while correcto:
            print("Introduce la categoria (RUEDAS, FRENOS, ASIENTO, CUADRO, DELANTERA, TRASERA, OTROS)")
            categoria=input()
            correcto=self._controlador.comprobarCategoria(categoria.upper())
            if correcto:
                print("Escribe una de las categroias mencionadas anteriormente")
        self._controlador.crearReparacionBicicleta(e, usuario, listado, fecha, coste, descripcion, categoria.upper())
    
    def mostarFamilia(self, familia):
        print("Tu familia es la siguiente:")
        try:
            print("Pareja: ", self._controlador.obtenerSocio(familia["Pareja"])._nombreCompleto)
        except:
            print("Pareja: Ninguna")
        try:
            print("Primer Padre: ", self._controlador.obtenerSocio(familia["Padres"][0])._nombreCompleto)
            print("Segundo Padre: ", self._controlador.obtenerSocio(familia["Padres"][1])._nombreCompleto)
        except:
            print("Primer Padre: Ninguno")
            print("Segundo Padre: Ninguno")
        
        try:
            if familia["Hijos"]==[]:
                print("Hijo: Ninguno")
            else:
                for i in familia["Hijos"]:
                    print("Hijo: ", self._controlador.obtenerSocio(i)._nombreCompleto)
        except:
            print("Hijo: Ninguno")
        print("Pulsa Intro para continuar...")
        input()
            
    def mostrarDatosCuotas(self,cuotas):
        print("Tu historial de cuotas es el siguiente:")
        print("AÑO   PAGADO   PRECIO    DESCUENTO     FECHA PAGO  ")
        print("---------------------------------------------------")
        for dni, datos in cuotas.items():
                if (datos[2]==False):
                    print("{:<6}  {:<7} {:<11} {:<11}{:<10}".format(dni,"No" , datos[3], datos[4], datos[5]))
            
        for dni, datos in cuotas.items():
            if (datos[2]==True):
                print("{:<6}  {:<7} {:<11} {:<11} {:<10}".format(dni, "Si" , datos[3], datos[4], datos[5]))
        print("Pulsa Intro para continuar...")
        input()