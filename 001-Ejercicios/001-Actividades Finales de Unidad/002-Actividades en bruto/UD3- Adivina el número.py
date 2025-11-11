'''
	Número aleatorio
	v1.0 Daniel Oliveira Vidal
	Este programa piensa un número y tienes que tratar de adivinarlo
'''
import random

intentos = 6

numero = random.randint(1, 50)
respuesta = ''

print('Trata de adivinar el número que estoy pensando.')
print('Solo tendras 6 intentos.')
print('')

while respuesta != numero or intentos == 0:
	if intentos == 0:
		break
	
	else:
		respuesta = input('Dime un número del 1 al 50: ')
		print('')
		
		while True: 
			try:
				respuesta = int(respuesta)
			
				if respuesta < 1 or respuesta > 50:
					print('El numero esta fuera de rango')
					print('')
					break
			
				else:
					if respuesta != numero:
						print('Ese no es el número que estoy pensando.')
						intentos -= 1
						
						if respuesta > numero:
							print('El que me has dicho es demasiado alto.')
							print('')
							
						elif respuesta < numero:
							print('El que me has dicho es demasiado bajo.')
							print('')
						
						if intentos == 3:
							prueba_paridad = numero % 2
							if prueba_paridad == 0:
								print('El número secreto es par.')
								print('')
								
							else:
								print('El número secreto es impar.')
								print('')
								
						if intentos == 0:
							print('Te quedas sin intentos lo siento, el número era el', numero)
							print('')
							break
						
						else:
							print('Te quedan', intentos, 'intentos.')
							print('')
							break
						
					else:
						print('Correcto el número era el', numero, '.')
						print('')
						break
			
			except:
				try:
					respuesta = float(respuesta)
					assert isinstance(respuesta, (int, float))
					print('Ese no es un número valido')
					print('')
					break
					
				except:
					print('Ese no es un caracter valido')
					print('')
					break
