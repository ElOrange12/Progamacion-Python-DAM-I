'''
	Comprobante de partidos ganados
	v1.0 Daniel Oliveira Vidal
	Este programa te dice si el equipo visitante puede ganar y si la diferencia de goles
'''

goles_local = int(input('Dime los goles del equipo local: '))
goles_visitante = int(input('Dime los goles del equipo visitante: '))

assert goles_local > goles_visitante, 'El equipo visitante no puede ganar'

partido_tan_traumatico = int(input('Dime la diferencia de goles: '))

assert partido_tan_traumatico > 5, 'La diferencia de goles no puede ser tan grande'


