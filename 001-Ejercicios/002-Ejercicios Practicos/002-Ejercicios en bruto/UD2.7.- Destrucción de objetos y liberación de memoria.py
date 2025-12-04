'''
	Jugadores en cuadras
	v1.0 Daniel Oliveira Vidal
	Este programa divide a jugadores en cuadras y dice cuantas hace falta.
'''
import math as matematicas

jugadores_del_equipo = 0

jugadores_x_cuadra = 3

jugadores_del_equipo = int(input('Dime el número de jugadores que hay en tu equipo: '))

numero_de_cuadras = matematicas.ceil(jugadores_del_equipo / jugadores_x_cuadra)

print('Se necesitan un total de', numero_de_cuadras, 'cuadras.')


