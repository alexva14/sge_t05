from Modelo.SociosModelo import Socio
from Modelo.UsuarioModelo import Usuario
from Modelo.ClubModelo import Club

class Prueba: 
    def cargarSocios(club : Club):
        #self._listaSocios = {'11111111A' : Usuario ("admin", "C/admin", 666777888, "admin@gmail.com")}
        #def _init_(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas: Bicicleta, familia):
        club.asignarListaSocios({'12123123X' : Socio (club.getUsuario('12123123X'), 'Alex Valdepeñas', 'c/direccion2', 6666666666, "alex@gmail.com"),
        '11111111A' : Socio (club.getUsuario('11111111A'), 'Alejandro Montero', 'c/direccion1', 666777888, "alejandro@gmail.com"),
        '22222222B' : Socio (club.getUsuario('22222222B'), 'Fran Montero', 'c/direccion1', 111222333, "fran@gmail.com")})

    def cargarUsuarios(club : Club):
        club.asignarListaUsuarios( {'11111111A' : Usuario ('11111111A','admin', '24/01/2022', True), 
                                '22222222B' : Usuario ('22222222B', 'usuario1', '23/01/2022', False),
                                '12123123X' : Usuario ('12123123X', 'admin', '23/01/2022', True)})

    def cargarControlCuotas(club:Club):
        club._controlCuotas=({'12123123X' : (2022, club.getSocio('12123123X'), club.getUsuario('12123123X')._corriente_pago, 15, 0, "27-01-2022" ),
        '11111111A' : (2022, club.getSocio('11111111A'), club.getUsuario('11111111A')._corriente_pago, 15, 0, "27-01-2022" ),
        '22222222B' : (2022, club.getSocio('22222222B'), club.getUsuario('22222222B')._corriente_pago, 15, 0, "27-01-2022" )
        })