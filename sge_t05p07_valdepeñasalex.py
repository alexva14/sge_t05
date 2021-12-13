tiempo=""
segundos=0

print("Intoduce una hora en el sigueinte formato hh:mm:ss")
tiempo= input().split(":")
segundos= (int(tiempo[0])*60*60)+(int(tiempo[1])*60)+(int(tiempo[2]))
print(str(segundos)+ " segundos")