'''
	Mini aplicación
	v1.0 Daniel Oliveira Vidal
	Un mini-aplicación que guarda, muestra, actualiza y elimina clientes de una lista
'''
import pickle

class Cliente():
	def __init__ (self, nombre, apellidos, edad):
		self.nombre = nombre
		self.apellidos = apellidos
		self.edad = edad

clientes = []

try:
	archivo = open('BaseDeDatosClientes.bin', 'rb')
	clientes = pickle.load(archivo)
except:
	print('No existe archivo de datos')

while True:
	archivo = open('BaseDeDatosClientes.bin','wb')
	pickle.dump(clientes, archivo)
	archivo.close()	
		
	print('')
	print('Selecciona una opción:')
	print('1.-Añadir cliente.')
	print('2.-Mostrar clientes.')
	print('3.-Salir')
	print('')
	
	respuesta = int(input('Escoge una opción: '))
	print('')
	
	if respuesta == 1:				
		print('Vamos a insertar un cliente')
		nombre = input('Introduce el nombre: ')
		apellidos = input('Indroduce los apellidos: ')
		edad = input('Introduce el edad: ')
		
		clientes.append(Cliente(nombre, apellidos, edad))
		
		print('')
		
	elif respuesta == 2:
		identificador = 0
		for nuevocliente in clientes:
			print('Este es el cliente con ID:', identificador)
			print(nuevocliente.nombre, nuevocliente.apellidos, nuevocliente.edad)
			identificador += 1
		print('')

	elif respuesta == 3:
		print('Hasta luego')
		print('')
		break
	
	else:
		print('Esa respuesta no es valida')
		print('')

