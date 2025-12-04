def raizSegura(numero):
	'''
		Función raizSegura
		Entradas: Radicando que se espera que se un número
		Salida: El resultado dependerá en el literal que entra a la función:
			1.- Si es numérico ---> Devolverá la raíz del número
			2.- Si se puede convertir a numérico ---> Devolverá la raíz del número
			3.- Si es numérico pero negativo ---> Devolverá 0
			4.- Si no se puede convertir a numérico ---> Devolverá 0 
	'''
	from math import sqrt

	if isinstance(numero, (int, float)):
		if numero >= 0:
			raiz_numero = sqrt(numero)
			return raiz_numero
		else:
			assert numero >= 0, 'El número es negativo'
			return 0
			
	else:
		try:
			numero = float(numero)
			raiz_numero = sqrt(numero)
			return raiz_numero
			
		except:
			return 0
			assert isinstance(numero, (float)), 'No se ha convertido a numérico'
