import math
class Punto:
    x=0
    y=0

    def __init__(self, x, y):
        self.x= x
        self.y=y
    
    def __str__(self):
        return  "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(self, "pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(self, " pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(self, " pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(self, " pertenece al cuarto cuadrante")
        elif self.x != 0 and self.y == 0:
            print(self, " se sitúa sobre el eje X")
        elif self.x == 0 and self.y != 0:
            print(self, " se sitúa sobre el eje Y")
        else:
            print(self, " se encuentra sobre el origen")
    
    def vector(self, p):
        print("El vector entre ", self, " y ", p, " es (", p.x - self.x,"," ,p.y - self.y,")")

    def distancia(self, p):
            d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
            print("La distancia entre los puntos {} y {} es {}".format(
                self, p, d))
    
class Rectangulo:
    inicial=0
    final=0

    def __init__(self,inicial, final):
        self.inicial = inicial
        self.final = final

    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )


#PROBAMOS NUESTRO PROGRMA
puntosCorrecto=False
while not puntosCorrecto:
    print("Introduce el punto x del primer punto")
    x1=input()
    print("Introduce el punto y del primer punto")
    y1=input()
    print("Introduce el punto x del segundo punto")
    x2=input()
    print("Introduce el punto y del segundo punto")
    y2=input()
    
    if x1==x2 and y1==y2:
        print("Los puntos son iguales, introduce otros") 
    else:
        puntosCorrecto=True
        p1= Punto(x1,y1)
        p2= Punto(x2,y2)

opcionElegida=0
while opcionElegida != 7:
    try:
        
        print("1) Operaciones con puntos. Muestra el siguiente submenú:")
        print("2) Operaciones con puntos. Muestra el siguiente submenú:")
        print("3) Salir ")

        opcion2=""
        if opcionElegida==1:
            print("     1.Mostrar cuadrante al que pertenecen")
            print("     2.Calcular vector.")
            print("     3.Calcular distancia")

            if opcion2==1:
                print()

            if opcion2==2:
                print() 
            else:
                print("Hasta luego!")

        if opcionElegida==2:
            print("     1.Calcular base")
            print("     2.Calcular altura")
            print("     3.Calcular área.")
        if opcionElegida==3:
           print("Hasta luego!")

    except ValueError: 
        print("Debes introducir un número del 1 al 3")
