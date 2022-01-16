import os
from sge_t05p01_e26_valdepeñasalex.controlador.Movimiento import Movimiento

class Cuenta:
    cuenta=0
    numero_cuenta=cuenta
    dni=0
    titular=0
    saldo=0
    movimientos=[]

    

    def __init__(self, dni, titular, saldo):
        self.dni=dni
        self.titular=titular
        self.saldo= saldo
        self.cuenta= Cuenta.cuenta+1
        Cuenta.cuenta+=1
        self.numero_cuenta=self.cuenta
        
    def imprimir_cuenta(self):
        print("Numero de cuenta: ", self.numero_cuenta)
        print("DNI titular: ", self.dni)
        print("Nombre titular: ", self.titular)
        print("Saldo cuenta: ", self.saldo)
        print("Movimientos de la cuenta: ")

        for i in self.movimientos:
            print("Fecha:", Movimiento(i).fecha)
            print("Cantidad:",Movimiento(i).cantidad)
            print("Ingreso:",Movimiento(i).ingreso)
            print("Concepto:",Movimiento(i).concepto)

    def hacer_movimiento(self, movimiento):
        if Movimiento(movimiento).ingreso: 
            self.saldo= self.saldo + Movimiento(movimiento).cantidad
            return True
        else:
            if Movimiento(movimiento).cantidad > self.saldo:
                return False
            else:
                self.saldo= self.saldo - Movimiento(movimiento).cantidad
                return True

if __name__ == "__main__":
    os.system ("cls")
    print("Test")
