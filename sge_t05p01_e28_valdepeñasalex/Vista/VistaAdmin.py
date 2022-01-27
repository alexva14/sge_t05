import sys
from datetime import date

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

    def mostrarMenu(self, usuario):
        print("Menú Admin:") 
        print("")
        print("************************************************")
        print("*              LOS SATANASES DEL               *")
        print("*                INFIERNO APP                  *")
        print("************************************************")
        print("*            Zona de administración            *")
        print("*                Usuario: ",usuario,"          *")
        print("*                Último acc.:                  *")
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
        print("9. Realizar el control de cuotas")
        print("0. Salir.")
        self.leerOpcionMenu()
        
    
    def leerOpcionMenu(self):
        opc=0
        try:
            opc=int(input("Deme una opción: "))
            
        except:
            print("Debes introducir un número entero.")
        if (opc >=0 and opc <=9):
            #return opc
            self._controlador.ControlOpciones(opc)
        else:
            print("Debes introducir un número entero entre 0 y 9.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def mostrarSocios(self,lista_socios):
        print("->Nombre de nuestros socios<-")
        for nombre in sorted(lista_socios):
            print("- ",nombre)
    
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
        if (admin.lower=="si"):
            admin=True
        else:admin=False
        print("Introduce el nombre completo del nuevo socio")
        nombre=input()
        print("Introduce una direccion")
        direccion=input()
        print("Introduce un numero de telefono")
        telefono=int(input())
        print("Introduce el correo electronico")
        correo=input()
        self._controlador.crearSocUser(dni, contrasenna, admin, nombre, direccion, telefono, correo)
    
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
                print("Este usuario ya dispone de una pareja asignada")
        else:print("Debes introducir un número entero entre 0 y 9.")
    
    def pedirDatosPareja(self, dnipareja1):
        correcto=True
        while correcto:
            print("Introduce el dni de la pareja (debe ser socia del club): ")
            dnipareja2=input()
            correcto=self._controlador.comprobarExisteDni(dnipareja2)
            correcto=False
            if (dnipareja2==dnipareja1):
                print("Un usuario no se puede tener de paereja a si mismo")
                correcto=True            
            if not correcto:
                correcto=False
        #self._controlador.añadirPareja()
            

