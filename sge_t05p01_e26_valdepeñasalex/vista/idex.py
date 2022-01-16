from sge_t05p01_e26_valdepeñasalex.controlador.Banco import Banco
from sge_t05p01_e26_valdepeñasalex.controlador.Movimiento import Movimiento
from sge_t05p01_e26_valdepeñasalex.modelo.Prueba import Prueba
from sge_t05p01_e26_valdepeñasalex.controlador.Cuenta import Cuenta

#creo el banco
banco1= Banco("Banco GP", None)

#cargo los datos
Prueba.cargar_datos(banco1)

#iniciamos el bucle

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

            #vamos a comprobar el dni si existe o no
            for cuenta in banco1.cuentas:
                if Cuenta(cuenta).dni==dni:
                    print("Este cliente ya dispone de una cuenta")
                else:
                    print("Dni no repetido")
                    correcto= True
            
            print("Introduce el nombre del cliente:")
            nombre=input()
            print("Introduce el saldo inicial:")
            saldo= int(input())
            cuenta= Cuenta(dni, nombre, saldo)
            banco1.cuentas.append(cuenta)

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
