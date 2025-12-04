'''
	Division con fix de DIVISION x 0
	v1.0 Daniel Oliveira Vidal
	Este programa prueba ha hacer una división, si esta falla muestra un error y continua.
'''

print('Vamos a hacer una división')

a = float(input('Dime el dividendo; '))
b = float(input('Dime el divisor: '))

try:
	print(a / b)
except:
	print('No se puede dividir entre 0')
	
print('Hemos terminado de operar')
