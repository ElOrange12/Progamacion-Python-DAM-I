'''
    Clase PartidoFutbol
    v1.0 Daniel Oliveria Vidal
    Este programa crea una clase, con la cual se puede instanciar dos nombre de equipos de fútbol y llamar a un metodo que te diga quien jugo ese partido.
'''

class PartidoFutbol():
    def __init__(self):
        self.nombre_equipo_local = ''
        self.nombre_equipo_visitante = ''

    def mostrar_info(self):
        print('El partido lo jugaron los equipos:', self.nombre_equipo_local, 'y', self.nombre_equipo_visitante)

clasico = PartidoFutbol()
clasico.nombre_equipo_local = 'FC Barcelona'
clasico.nombre_equipo_visitante = 'Real Madrid'
clasico.mostrar_info()

semis_champions = PartidoFutbol()
semis_champions.nombre_equipo_local = 'Manchester United'
semis_champions.nombre_equipo_visitante = 'Juventus'
semis_champions.mostrar_info()