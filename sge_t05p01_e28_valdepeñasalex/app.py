import sys
from Controlador.AdminController import ControladorAdmin
from Controlador.UserController import ControladorUser
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba

if __name__ == "__main__":
    #creamos el club
    club= Club("Los satanases del Infierno", 13230)
    #argumentos=["app.py","-u", "11111111A", "-p", "admin", "-A"]
    #argumentos=["app.py","-u", "22222222B", "-p", "usuario1"]
    argumentos=sys.argv

    if (club.verificarUsuarioAdmin(argumentos)):
        controlador = ControladorAdmin(club, argumentos[2], argumentos[4])
    else:
        controlador = ControladorUser(club, argumentos[2], argumentos[4])

