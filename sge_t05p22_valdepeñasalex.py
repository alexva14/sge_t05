from collections import defaultdict

palabra=""
lista=[]
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
print(result)