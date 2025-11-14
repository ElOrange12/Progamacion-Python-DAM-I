'''
	CRUD clientes
	v1.0
	Este programa es un ejemplo de CRUD de una lista de clientes
'''

class Cliente():
	def __init__(self):
		self.email = None
		self.nombre = None
		self.direccion = None
		
cliente1 = Cliente()

email = input('Dime el email del cliente: ')
nombre = input ('Dime el nombre del cliente: ')
direccion = input('Dime la dirección del cliente: ')

cliente1.email = email
cliente1.nombre = nombre
cliente1.direccion = direccion

print(cliente1)

clientes = []

while True:
	print('1.-Insertar un cliente\n2.-Listar clientes\n3.-Actualizar clientes\n4.-Eliminar clientes')
	respuesta = int(input('Elige una opción: '))
	
	if respuesta == 1:
		email = input('Dime el email del cliente: ')
		nombre = input ('Dime el nombre del cliente: ')
		direccion = input('Dime la dirección del cliente: ')

		cliente1.email = email
		cliente1.nombre = nombre
		cliente1.direccion = direccion
		
		clientes.append(cliente1)
	
	elif respuesta == 2:
		for cliente in clientes:
			print(cliente)
	
	elif respuesta == 3:
		
	
	elif respuesta == 4:
		
	
