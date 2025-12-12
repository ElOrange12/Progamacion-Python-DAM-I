dividendo = 4
divisor = 0

try:
	division = dividendo/divisor
except ZeroDivisionError:
	print('No se puede dividir entre 0')
except Exception as mierror:
	print('Hay un error')
