import sys
from Modelo.ClubModelo import Club
from Modelo.Prueba import Prueba
from Controlador.AdminController import ControladorAdmin
from Controlador.UserController import ControladorUser
import json

if __name__ == "__main__":

    #club =Club("Los Satanases del Infierno", 13230)
    
    #creamos el club sge_t05p01_e28_valdepeñasalex/
    with open("sge_t05p01_e28_valdepeñasalex/club.json", 'r') as f:
        cadjson=json.load(f)
    for i in cadjson:
        club=Club(i["_nombreClub"],i["_cif"],i["_sedeSocial"],i["_saldoTotal"],i["_controlCuotas"])
    

    argumentos=["app.py","-u", "11111111A", "-p", "admin", "-A"]
    #argumentos=["app.py","-u", "11111111A", "-p", "admin"]
    #argumentos=sys.argv

    if(argumentos[1]=="-u" and argumentos[3]=="-p"):
        if (club.verificarUsuarioAdmin(argumentos)):
            controlador = ControladorAdmin(club, argumentos[2], argumentos[4])
        elif (club.verificarUsuarioUser(argumentos)):
            controlador = ControladorUser(club, argumentos[2], argumentos[4])
    else:
        print("Los argumentos deben ser -u y -p")
