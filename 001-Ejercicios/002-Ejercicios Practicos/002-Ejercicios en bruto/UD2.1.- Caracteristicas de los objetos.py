'''
	Equipos de fútbol
	v1.0 Daniel Oliveira Vidal
	Este programa define una clase que se refiere a un equipo de futbol, calcula la distancia entre dos jugadores, hace una función de simulación de partido y por ultimo hace instancias de dos equipos y simula el partido con estos dos.
'''
from math import sqrt

class EquipoFutbol():
	def __init__(self):
		self.nombre = ''
		self.ciudad = ''
		self.jugadores = []
		
pj1 = (2, 1)
pj2 = (4, 3)

distancia_jugadores = sqrt((pj1[1] - pj1[0])**2 + (pj2[1] - pj2[0])**2)

def partidoFutbol(Equipo1, Equipo2):
	'''
		función partidoFutbol
		Entradas: El nombre de dos equipos
		Salidas: Goles hecho por el primer equipo y el segundo y dice que gana el primero
	'''
	goles_equipo_1 = 0
	goles_equipo_2 = 0
	
	for i in range(0, 4):
		goles_equipo_1  += 1
	
	print('El', Equipo1, 'a marcado', goles_equipo_1, 'goles')
	
	for i in range(0, 3):
		goles_equipo_2 += 1
		
	print('El', Equipo2, 'a marcado', goles_equipo_2, 'goles')
		
	ganador = Equipo1
	
	return ganador
	
equipo_favorito = EquipoFutbol()
equipo_favorito.nombre = 'FC_Barcelona'
equipo_favorito.ciudad = 'Barcelona'
equipo_favorito.jugadores.append('Pedri')

equipo_rival = EquipoFutbol()
equipo_rival.nombre = 'Real Vardrid'
equipo_rival.ciudad = 'Madrid'
equipo_rival.jugadores.append('Valverde')

print('El ganador es', partidoFutbol(equipo_favorito.nombre, equipo_rival.nombre))
