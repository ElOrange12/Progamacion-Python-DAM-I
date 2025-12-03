'''
	Clase jugador
	v1.0 Daniel Oliveira Vidal
	Este programa define una clase sencilla.
'''

class Jugador():
	def __init__(self):
		self.nombre = ''
		self.genero_favorito = ''
		self.horas_jugadas = 0
		
	def setNombre(self, nuevonombre):
		self.nombre = nuevonombre
		
	def mostrarNombre(self):
		print(self.nombre)		
