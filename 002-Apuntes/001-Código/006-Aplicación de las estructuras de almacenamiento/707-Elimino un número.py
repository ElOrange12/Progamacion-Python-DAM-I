import random

patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}

while True:
	lista = []
	for i in range (1,10):
		lista.append(random.randint(1, 9))
	conjunto = set(lista)
	print(lista)
		
	if conjunto == patron:
		print('El conjunto es correcto')
		print(conjunto)
		print(lista)
		# Ahora elimino un número
		indice = random.randint(0,8)
		lista[indice] '_' # Escoge un indice al azar y reemplaza su valor
		print(lista)
		break # Fuerza la finalización del bucle infinito
