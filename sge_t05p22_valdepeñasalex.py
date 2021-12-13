from collections import defaultdict

palabra=""
lista=[]

#alamcenamos todas las palabras en una lista
while palabra !="salir":
    print("Escribe un fabricante de dispositivos moviles")
    palabra=input()
    if palabra != "salir": 
        lista.append(palabra)

#recorremos la lista en busca de elementos repetidos
aux = defaultdict(list)
for index, item in enumerate(lista):
    aux[item].append(index)
result = {item: indexs for item, indexs in aux.items() if len(indexs) > 1}

#comprobamos si el diccionario
if bool(result):
    print("Hay elementos reptidos")
    print(result)
else:
    print("No hay elementos repetidos en esta lista")

listaordenada= sorted(lista)

if lista==listaordenada:
    print("Lista ordenada")
else:
    print("Lista no ordenada alfabeticamente")
    
