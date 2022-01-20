from modelo.Banco import Banco
from modelo.Prueba import Prueba
from controlador.ControladorApp import Controlador

if __name__ == "__main__":
    cuentas=[]
    banco1= Banco("Banco GP", cuentas )

    #cargo los datos
    Prueba.cargar_datos(banco1)

    controlador_app = Controlador(banco1)