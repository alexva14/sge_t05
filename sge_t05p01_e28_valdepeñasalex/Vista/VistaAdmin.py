import sys
from datetime import date
from datetime import datetime

class VistaAdmin:
    def __init__(self, contr): 
        self._controlador=contr

    def inicio(self):
        fdate = date.today().strftime('%d/%m/%Y')
        print("Bienvenido. Hoy es: {}".format(fdate))
        self.mostrarMenu()
        try:
            opc=self.leerOpcionMenu()
            self._controlador.ControlOpciones(opc)
        except Exception as exc:
                self.mostrarError(exc)
        finally:
                self.salir

    def mostrarMenu(self, usuario, fecha):
        print("Menú Admin:") 
        print("")
        print("************************************************")
        print("*              LOS SATANASES DEL               *")
        print("*                INFIERNO APP                  *")
        print("************************************************")
        print("*            Zona de administración            *")
        print("*                Usuario: ",usuario,"          *")
        print("*                Último acc.:",fecha,"      *")
        print("************************************************")
        print("")
        print("====")
        print("1. Ver listado completo de socios")
        print("2. Insertar un nuevo socio")
        print("3. Añadir familia a un socio")
        print("4. Ver listado completo de los próximos eventos")
        print("5. Buscar eventos")
        print("6. Insertar un nuevo evento")
        print("7. Ver control de cuotas")
        print("8. Actualizar el control de cuotas")
        print("9. Realizar el pago de una cuota por DNI de socio")
        print("0. Salir.")
        self.leerOpcionMenu(usuario)
        
    
    def leerOpcionMenu(self, usuario):
        opc=0
        try:
            opc=int(input("Deme una opción: "))
            
        except:
            print("Debes introducir un número entero.")
        if (opc >=0 and opc <=9):
            #return opc
            self._controlador.ControlOpciones(opc, usuario)
        else:
            print("Debes introducir un número entero entre 0 y 9.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def mostrarSocios(self,lista_socios):
        print("->Nombre de nuestros socios<-")
        for nombre in sorted(lista_socios):
            print("- ",nombre)
        print("Pulsa Intro para continuar...")
        input()
    
    def salir(self):
        print("Cerrando aplicación...")
        sys.exit()

    def pedirDatosSocio(self):
        correcto=False
        while not correcto:
            print("Introduce el dni del nuevo socio")
            dni=input()
            correcto=self._controlador.comprobarExisteDni(dni)
            if not correcto:
                print("El dni esta ya introducido")
        print("Introduce la contraseña:")
        contrasenna=input()
        print("¿Es admin el usuario? ")
        admin=input()
        if (admin.lower()=="si"):
            admin=True
        else:admin=False
        print("Introduce el nombre completo del nuevo socio")
        nombre=input()
        print("Introduce una direccion")
        direccion=input()
        correcto= True
        while correcto:
            try:
                print("Introduce un numero de telefono")
                telefono=int(input())
                correcto=False
            except:
                print("Introduce numeros por favor")
        
        print("Introduce el correo electronico")
        correo=input()
        self._controlador.crearSocUser(dni, contrasenna, admin, nombre, direccion, telefono, correo)
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirDatosFamiliar(self):
        correcto=True
        while correcto:
            print("Introduce el dni de un socio al que quieras introducir familiares: ")
            dnipareja1=input()
            correcto=self._controlador.comprobarExisteDni(dnipareja1)
            if not correcto:
                correcto=False
        print("Elige que quieres añadir: ")
        print("1. Pareja")
        print("2. Hijos")
        print("3. Padres")
        opc=0
        try:opc=int(input("Deme una opción: "))  
        except:print("Debes introducir un número entero.")
        if (opc >=1 and opc <=3):
            accion=self._controlador.añadirFamiliares(opc, dnipareja1)
            if accion==1:
                print("Este usuario ya dispone de una pareja asignada o tiene padres asignados")
            if accion==2:
                print("Primero debes asignar una pareja a este cliente")
            if accion==3:
                print("Este usuario ya tiene dos hijos asociados")
            if accion==4:
                print("Este usuario ya dispone de una pareja asignada o tiene padres asignados")
        else:print("Debes introducir un número entero entre 0 y 9.")
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirDatosPareja(self, dnipareja1):
        correcto=True
        while correcto:
            print("Introduce el dni de la pareja (debe ser socia del club): ")
            dnipareja2=input()
            correcto=self._controlador.comprobarExisteDni(dnipareja2)
            #correcto=False
            if (dnipareja2==dnipareja1):
                print("Un usuario no se puede tener de paereja a si mismo")
                correcto=True            
            if not correcto:
                correcto=False
        self._controlador.añadirPareja(dnipareja1, dnipareja2)

    def pedirDatosHijo(self, dnipareja1):
        correcto=True
        while correcto:
            print("Introduce el dni del hij@ (debe ser soci@ del club): ")
            dnihijo=input()
            correcto=self._controlador.comprobarExisteDni(dnihijo)
            #correcto=False
            if (dnihijo==dnipareja1):
                print("Un usuario no se puede tener de hijo a si mismo")
                correcto=True            
            elif (self._controlador.comprobarPadres(dnihijo)):
                print("Este usuario ya tiene unos padres asociados")
            if not correcto:
                correcto=False
        self._controlador.añadirHijo(dnipareja1, dnihijo)
    
    def pedirDatosPadres(self, dniuser):
        correcto=True
        while correcto:
            print("Introduce el dni de uno de los padres: ")
            dnipareja2=input()
            correcto=self._controlador.comprobarExisteDni(dnipareja2)
            #correcto=False
            if (not correcto):
                if (dnipareja2==dniuser):
                    print("Un usuario no se puede tener de padre a si mismo")
                    correcto=True
                if(self._controlador.comprobarPadre(dnipareja2, dniuser)):
                    print("Un usuario no puede tenre más de dos padres")
                    correcto=True
                else:
                    correcto=False               
        self._controlador.añadirPadres(dniuser, dnipareja2)
        
    def mostrarEventos(self, lista):
        print("Eventos para los proximos días:")
        for i in lista:
            print("Fecha: ",i._fechaEvento)
            print("Fecha maxima inscripción: ",i._fechaMaxInscripcion)
            print("Localidad: ", i._localidad)
            print("Provincia: ", i._provincia)
            print("Organización: ", i._organizador)
            print("KM Totales: ",i._kmTotales)
            print("Precio: ",i._precio)
            print("-----------------------")
        print("Pulsa Intro para continuar...")
        input()

    def pedirFecha(self):
        correcto= True
        while correcto:
            try:
                print("Introduce la fecha (dia/mes/año es decir **/**/****)")
                fecha=input()
                prueba=datetime.strptime(fecha,'%d/%m/%Y')
                correcto=False
            except:
                print("Introduce una fecha correcta")
        evento=self._controlador.buscarEvento(fecha)
        for i in evento:
            print("Fecha: ",i._fechaEvento)
            print("Fecha maxima inscripción: ",i._fechaMaxInscripcion)
            print("Localidad: ", i._localidad)
            print("Provincia: ", i._provincia)
            print("Organización: ", i._organizador)
            print("KM Totales: ",i._kmTotales)
            print("Precio: ",i._precio)
            print("Socios: ")
            for e in i._listadoSociosApuntados:
                print("-DNI: ", e)
            print("=================================")
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirDatosEventos(self):
        correcto= True
        while correcto:
            try:
                print("Introduce la fecha de inicio del evento (dia/mes/año es decir **/**/****)")
                fecha_inicio=input()
                prueba=datetime.strptime(fecha_inicio,'%d/%m/%Y')
                correcto=False
            except:
                print("Introduce una fecha correcta")
        correcto= True
        while correcto:
            try:
                print("Introduce la fecha final de inscripcion evento (dia/mes/año es decir **/**/****)")
                fecha_ins=input()
                prueba=datetime.strptime(fecha_ins,'%d/%m/%Y')
                if(datetime.strptime(fecha_inicio,'%d/%m/%Y'))>=(datetime.strptime(fecha_ins,'%d/%m/%Y')):
                    correcto=False
                else:
                    print("La fecha de fin de inscripción debe ser anterior a la fecha del evento")
            except:
                print("Introduce una fecha correcta")
        print("Lugar del evento: ")
        lugar=input()
        print("Provincia del evento: ")
        provincia=input()
        print("Organización: ")
        organizacion=input()
        print("Distancia a recorrer: ")
        distancia=int(input())
        print("Precio de inscipción: ")
        precio=int(input())
        socios=[]
        self._controlador.crearEvento(fecha_inicio, fecha_ins, lugar, provincia, organizacion, distancia, precio, socios)
        print("Evento creado con exito!!")
        print("Pulsa Intro para continuar...")
        input()
    
    def pedirAñoControlCuotas(self):
        correcto=True
        while correcto:
            print("Introduce el año que quieres visualizar:")
            try:
                año=int(input())
                correcto=False
            except:
                print("Introduce un año correcto por favor")
        return año
    
    def mostrarControlCuotas(self,cuotas, club):
        try:
            print("DATOS DE LAS CUOTAS")
            print("   DNI       AÑO      NOMBRE            PAGADO   PRECIO        DESCUENTO    FECHA PAGADO")
            for dni, datos in cuotas.items():
                if (datos[2]==False):
                    print("{:<12} {:<7} {:<20} {:<8} {:<15} {:<11}{:<10}".format(dni, datos[0], club.getSocio(datos[1])._nombreCompleto, "No" , datos[3], datos[4], datos[5]))
            
            for dni, datos in cuotas.items():
                if (datos[2]==True):
                    print("{:<12} {:<7} {:<20} {:<8} {:<15} {:<10} {:<10}".format(dni, datos[0], club.getSocio(datos[1])._nombreCompleto, "Si" , datos[3], datos[4], datos[5]))
        except:
            print("No hay datos de este año")
        print("Pulsa Intro para continuar...")
        input()
    
    def mostrarMensaje(self, string):
        print(string)
        print("Pulsa Intro para continuar...")
        input()

    def pedirPagarCuota(self):
        correcto=True
        while correcto:
            print("Introduce el dni del usuario al que quieres pagar la cuota")
            dni=input()
            correcto=self._controlador.comprobarExisteDni(dni)
            if not correcto:
                correcto=False
            else:
                print("Este usuario no existe")
        #comprobamos si el año en curso esta en eñ control de cuotas
        existe=self._controlador.comprobarControlCuotas()
        if existe:
            self.mostrarMensaje("El control de cuotas de este año ya estaba creado")
        else:
            self._controlador.crearControlCuotasAño()
            self.mostrarMensaje("El control de cuotas del año en curso ha sido creado con los datos nuevos")
        #comrpobamos si este usuario tiene pagada la cuota
        pagado=self._controlador.comprobarPagado(dni)
        if pagado:
            print("Este usuario ya tiene pagada la cuota")
        else:
            print("Vamos a proceder con el pago")
            print("El total a pagar es: ",self._controlador.obtenerCantidadPagar(dni))
            print("Pagado....")
            self._controlador.pagarCuota(dni)
        print("Pulsa Intro para continuar...")
        input()