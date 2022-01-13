import datetime
class Fecha: 
    dia=0
    mes=0
    anno=0

    def __init__(self, dia, mes, anno):
        self.dia= dia
        self.mes= mes
        self.anno= anno


    def actual(self):
        x = datetime.datetime.now()
        return self(x.day, x.month, x.year)


