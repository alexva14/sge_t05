tiempo=""
segundos1=0
segundos2=0

print("Intoduce una hora en el sigueinte formato hh:mm:ss")
tiempo= input().split(":")
segundos1= (int(tiempo[0])*60*60)+(int(tiempo[1])*60)+(int(tiempo[2]))
print(str(segundos1)+ " segundos")

print("Intoduce una hora en el sigueinte formato hh:mm:ss")
tiempo= input().split(":")
segundos2= (int(tiempo[0])*60*60)+(int(tiempo[1])*60)+(int(tiempo[2]))
print(str(segundos2)+ " segundos")

print("La diferencia en segundos entre los dos tiempos es: " + str(abs(segundos1-segundos2))+ " segundos")