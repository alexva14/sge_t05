
from modelo.Movimiento import Movimiento
from modelo.Cuenta import Cuenta

#iniciamos el bucle

class Vista:
    def __init__(self, contr): 
        self._controlador=contr

    def inicio(self):
        opcionElegida=0
        while opcionElegida != 6:
            print("1. Nuevo cliente y saldo de partida")
            print("2. Buscar y mostrar una cuenta por dni o por número")
            print("3. Buscar cuentas con un saldo superior a una cantidad dada")
            print("4. Añadir un movimiento a una cuenta por dni")
            print("5. Mostrar información completa del Banco")
            print("6. Salir")

            print("Elige una opcion: ")
            opcionElegida=int(input())

            if (opcionElegida==1):
                correcto= False
                while (correcto ==False):

                    print("Introduce el dni del nuevo cliente: ")
                    dni= input()
                    correcto=self._controlador.comprobarDNI(dni)
                    if (correcto):
                        print("Este DNI no esta registrado")
                    else:
                        print("Este DNI ya esta registrado")
                        continue
                    
                    print("Introduce el nombre del cliente:")
                    nombre=input()
                    print("Introduce el saldo inicial:")
                    saldo= int(input())
                    self._controlador.crearCuenta(nombre, saldo, dni)
                    correcto=True

            if (opcionElegida==2):
                print("Buscar por: ")
                print("1. DNI")
                print("2. Numero")
                print("Opción: ")
                opcion=int(input())
                if (opcion==1):
                    print("Introduce el dni: ")
                    dni= input()
                    for cuenta in banco1.cuentas:
                        if Cuenta(cuenta).dni==dni:
                            print(Cuenta(cuenta).dni)
                            print(Cuenta(cuenta).titular)
                            print(Cuenta(cuenta).saldo)
                            print(Cuenta(cuenta).numero_cuenta)
                else:
                    print("Introduce el numero: ")
                    numero= int(input())
                    for cuenta in banco1.cuentas:
                        if Cuenta(cuenta).numero_cuenta==numero:
                            print(Cuenta(cuenta).dni)
                            print(Cuenta(cuenta).titular)
                            print(Cuenta(cuenta).saldo)
                            print(Cuenta(cuenta).numero_cuenta)
            
            if (opcionElegida==3):
                print("Introduce un saldo: ")
                saldo=int(input())
                for cuenta in banco1.cuentas:
                    if Cuenta(cuenta).saldo>saldo:
                        print(Cuenta(cuenta).dni)
                        print(Cuenta(cuenta).titular)
                        print(Cuenta(cuenta).saldo)
                        print(Cuenta(cuenta).numero_cuenta)

            if (opcionElegida==4):
                print("Introduce el dni: ")
                dni= input()
                for cuenta in banco1.cuentas:
                    if Cuenta(cuenta).dni==dni:
                        print("Introduce la cantidad del movimiento:")
                        cantidad=int(input())
                        print("Es un ingreso o retirada:")
                        opcion=input()
                        print("Escribe un motivo")
                        motivo=input()
                        if opcion=="ingreso":
                            movimiento= Movimiento(cantidad, True, motivo)
                            Cuenta(cuenta).movimientos.append(movimiento)
                            Cuenta(cuenta).saldo= Cuenta(cuenta).saldo + cantidad
                        else:
                            if  Cuenta(cuenta).saldo-cantidad<0:
                                print("Este movimiento no se puede realizar")
                            else:
                                movimiento= Movimiento(cantidad, False, motivo)
                                Cuenta(cuenta).movimientos.append(movimiento)
                                Cuenta(cuenta).saldo= Cuenta(cuenta).saldo - cantidad
                    else:
                        print("Este dni no dispone de ninguna cuenta")
            
                if (opcionElegida==5):
                    print("Nombre: ", banco1.nombre)
                    print("Saldo total: ",banco1.saldo_total)
                    print("Datos de las diferentes cuentas: ")
                    for cuenta in banco1.cuentas:
                        print(Cuenta(cuenta).dni)
                        print(Cuenta(cuenta).numero_cuenta)
                        print(Cuenta(cuenta).saldo)
                        print(Cuenta(cuenta).titular)

                if (opcionElegida==6):
                    print("Programa finaliado, chao")
                    break
