from modelo.Banco import Banco
from modelo.Cuenta import Cuenta
from vista.idex import Vista

class Controlador:
    def __init__(self, banco: Banco):
        self._banco=banco
        self._vista=Vista(self)
        self._vista.inicio()

    def comprobarDNI(self, dni):
        correcto=False
        for cuenta in self._banco.cuentas:
            if cuenta.dni==dni:
                return correcto
        return True
    
    def crearCuenta(self, nombre, saldo, dni):
        cuenta= Cuenta(dni, nombre, saldo)
        self._banco.cuentas.append(cuenta)
