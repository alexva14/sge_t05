import Cuenta
class Banco:
    nombre=""
    cuentas=[]
    saldo_total=0

    def __init__(self, nombre, cuentas):
        self.nombre= nombre
        self.cuentas= cuentas

    def existe_cliente(self, dni):
        existe=False
        for cuenta in self.cuentas:
            if (Cuenta(cuenta).nombre ==dni):
                existe=True
        return existe
