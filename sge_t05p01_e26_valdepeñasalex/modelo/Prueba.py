from sge_t05p01_e26_valdepeñasalex.controlador.Banco import Banco
from sge_t05p01_e26_valdepeñasalex.controlador.Cuenta import Cuenta
from sge_t05p01_e26_valdepeñasalex.controlador.Movimiento import Movimiento
class Prueba:
    def cargar_datos(self, banco):
        cuenta1= Cuenta("71234567X", "Alex", 5000)
        cuenta2= Cuenta("11111111X", "Eseer", 100)
        cuenta3= Cuenta("22222222X", "Ramon", 30000)
        
        movimiento1=Movimiento(50, True, "Ingresos pasivos")
        movimiento2=Movimiento(50, False, "Ingresos pasivos")
        cuenta1.movimientos.append(movimiento1)
        cuenta1.movimientos.append(movimiento2)

        movimiento3=Movimiento(50, True, "Ingresos pasivos")
        movimiento4=Movimiento(50, False, "Ingresos pasivos")
        cuenta2.movimientos.append(movimiento3)
        cuenta2.movimientos.append(movimiento4)

        movimiento5=Movimiento(50, True, "Ingresos pasivos")
        movimiento6=Movimiento(50, False, "Ingresos pasivos")
        cuenta3.movimientos.append(movimiento5)
        cuenta3.movimientos.append(movimiento6)

        Banco(banco).cuentas.append(cuenta1)
        Banco(banco).cuentas.append(cuenta2)
        Banco(banco).cuentas.append(cuenta3)
        