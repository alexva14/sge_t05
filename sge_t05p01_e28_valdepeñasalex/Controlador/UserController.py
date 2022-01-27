from Vista.VistaUser import VistaUser
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba

class ControladorUser:
    def __init__(self,  club: Club, usuario, contrasenna):
        self._club=club
        self._vista=VistaUser(self)
        self.inicio(usuario, contrasenna)
        

    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)

        resultado=self._club.verificarUsuariosUs(usuario, contrasenna)
       
        if(resultado==1):
            self._vista.mostrarMenu()
        elif(resultado==2):
            self._vista.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vista.mostrarError("Este usuario no tiene permisos para acceder")