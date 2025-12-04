class Gato()
	def __init__(self, nombre, apellido, email, direccion): 	
		self.nombre = nombre
		self.apellido = apellido
		self.email = email
		self.direccion = direccion
		
clientes = []

while true:	
	nombre = input('Introduce el nombre del cliente: ')
	apellidos = input('Introduce los apellidos del cliente: ')
	email = input('Introduce el email del cliente: ')
	direccion = input('Introduce la direccion del cliente: ')

	clientes.appendCliente(nombre, apellidos, email, direccion)
