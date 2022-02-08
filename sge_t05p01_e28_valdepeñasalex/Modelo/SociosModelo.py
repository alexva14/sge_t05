from Modelo.UsuarioModelo import Usuario
from Modelo.BicicletaModelo import Bicicleta

class Socio: 
    def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas=None, familia={'Pareja': None,"Hijos":[],"Padres": []}):
        self._usuarioAsociado=usuarioAsociado
        self._nombreCompleto=nombreCompleto
        self._direccion=direccion
        self._telefono=telefono
        self._correoElectronico=correoElectronico
        self.bicicletas=bicicletas
        self.familia=familia
        #self.familia={'Pareja': None,
        #               "Hijos":[],
        #              "Padres": []}
    