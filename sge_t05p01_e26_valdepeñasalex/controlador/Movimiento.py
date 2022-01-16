from sge_t05p01_e26_valdepeñasalex.controlador.Fecha import Fecha

class Movimiento:
    fecha=0
    cantidad=0
    ingreso=False
    concepto=None

    def __init__(self, cantidad, ingreso, concepto):
        self.cantidad=cantidad
        self.ingreso=ingreso
        self.concepto=concepto
        self.fecha=Fecha.actual()
