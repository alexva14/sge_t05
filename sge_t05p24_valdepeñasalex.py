
#declaroamos el diccionario donde vamos a ir almacenando los clienes y daremos añadimos clientes
clientes= {}
clientes['71368908X']=['Alex','Valdepeñas Andujar', 'Calle Mayor 4', 678909987, 'alex@gmail.com', True]
clientes['123']=['Fran', 'Cozar Andujar', 'Mayor 4', 654678890, 'fran@gmail.com', False]

opcionElegida = 0

while opcionElegida != 7:
    try:
        
        print("Seleccione la operación que desea realizar")
        print("1) Añadir cliente")
        print("2) Eliminar cliente")
        print("3) Mostrar cliente")
        print("4) Listar todos los clientes")
        print("5) Listar clientes preferentes")
        print("6) Ordenar por apellidos")
        print("7) Terminar ")
        

        opcionElegida = int(input())

        if opcionElegida == 1:
            print("Vamos a añadir un nuevo cliente")
            dniCorrecto=False
            while not dniCorrecto:
                print("Introduce el dni")
                dni=input()
                
                if dni in clientes:
                    print("El DNI esta ya introducido en nuestra base de datos") 
                    
                else:
                    dniCorrecto=True
            print("Introduce el nombre")
            nombre=input()
            print("Introduce el apellido")
            apellido=input()
            print("Introduce el direccion")
            direccion=input()
            print("Introduce el telefono")
            telefono=input()
            print("Introduce el correo")
            correo=input()
            print("Introduce si es preferente o no")
            prioritario=bool(input())
            clientes[dni]=[nombre,apellido, direccion, telefono, correo, prioritario]

            
        elif opcionElegida == 2: 
            
            dniCorrecto=False
            while not dniCorrecto:
                print("Introduce el DNI del cliente que quieres eliminar")
                dniEliminar=input()
                if dniEliminar in clientes:
                    print("El DNI existe por lo que será eliminado")
                    dniCorrecto=True
                    del clientes[dniEliminar]
                else:
                    print("El DNI no existe")
                    

            
        elif opcionElegida == 3: 
            print("Introduce el DNI del cliente")
            dni=input()
            print("Los datos del cleinte son los sigueintes: ")
            print("Nombre: ", clientes[dni][0])
            print("Apellidos: ", clientes[dni][1])
            print("Direccion: ", clientes[dni][2])
            print("Telefono: ", clientes[dni][3])
            print("Correo: ", clientes[dni][4])
            print("Preferente: ", clientes[dni][5])
            print("")

            
        elif opcionElegida == 4: 
            print("Estos son todos los clientes que tenemos almacenados: ")
            for k, v in clientes.items():
                print("Dni: ", k, " Datos: ", v)
            
        elif opcionElegida == 5: 
            print("Estos son todos los clientes que tenemos almacenados que son preferentes: ")
            for k, v in clientes.items():
                if v[5]==True:
                    print("Dni: ", k, " Datos: ", v)

        elif opcionElegida == 6: 
            print("Estos son todos los clientes que tenemos almacenados (ordenados por apellido): ")
            listaOrdenada= sorted(clientes.items(), key=lambda item:item[1][1])
            print(listaOrdenada)
            

        elif opcionElegida == 7: 
            print("Hasta pronto!")
        
        elif opcionElegida<1 or opcionElegida>7:
            print("Introudce un numero entre el 1 y el 7 por favor")
        
    except ValueError: 
        print("Debes introducir un número del 1 al 3")
    
    
        