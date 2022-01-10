import datetime
class Fecha: 
    dia:0
    mes:0
    año:0
    fecha:0

    def __init__(self, dia, mes, año):
        self.dia= dia
        self.mes=mes
        self.año=año
        fecha = datetime.datetime (año, mes, dia)

    def actual(self):
        fecha = datetime.datetime.now()
