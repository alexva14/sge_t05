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
opcionElegida=0
while opcionElegida != 7:
    try:
        
        print("1) Operaciones con puntos. Muestra el siguiente submenú:")
        
        print("2) Operaciones con puntos. Muestra el siguiente submenú:")
        print("     a.Calcular base")
        print("     a.Calcular altura")
        print("     a.Calcular área.")
        print("3) Salir ")

        if opcionElegida==1:
            print("     a.Mostrar cuadrante al que pertenecen")
            print("     b.Calcular vector.")
            print("     c.Calcular distancia")
        if opcionElegida==1:
            print("     a.Mostrar cuadrante al que pertenecen")
            print("     b.Calcular vector.")
            print("     c.Calcular distancia")
        if opcionElegida==1:
            print("     a.Mostrar cuadrante al que pertenecen")
            print("     b.Calcular vector.")
            print("     c.Calcular distancia")
    except ValueError: 
        print("Debes introducir un número del 1 al 3")
