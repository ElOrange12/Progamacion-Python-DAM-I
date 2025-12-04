class Cliente():
	# Este es el método constructor
	def __init__ (self):
		self.nombrecompleto = ''
		self.email = ''
	# Estos son los setters y los getters
	def setNombreCompleto (self, nuevonombre):
		self.nombrecompleto = nuevonombre
	def setEmail (self, nuevoemail):
		self.email = nuevoemail
	def getNombreCompleto(self):
		return self.nombrecompleto	
	def getEmail (self):
		return self.email
		
# CRUD - Create, Read, Update, Delete
# CRUD SQL - Insert, Select, Update, Delete

clientes = [] 				############### Meto una lista de clientes vacía

print('Gestor de clientes v0.1 Daniel Oliveira Vidal')

while True: 
	print('Selecciona una opción: ')
	print('1.-Insertar un nuevo cliente')
	print('2.-Obtener listado de clientes')
	opcion = int(input('Indica tu opción (1,2): '))

	if opcion == 1:		# Los Setters se usan en las operaciones de creación de nuevos elementos
		print('Voy a insertar un cliente')
		nuevocliente = Cliente()
		nombrecliente = input('Introduce el nombre del cliente: ') # Tomo el dato
		nuevocliente.setNombreCompleto(nombrecliente) # Uso el metodo set para meter el dato en el objeto
		emailcliente = input('Introduce el email del cliente: ') # Tomo el dato
		nuevocliente.setEmail(emailcliente) # Uso el metodo ser para meter el dato en el objeto
		
		clientes.append(nuevocliente)
	elif opcion == 2: 
		print('Saco el listado de cliente')
		for cliente in clientes:
			print('--------------------')
			print('Nombre: ', cliente.getNombreCompleto())
			print('Email: ', cliente.getEmail())
			print('--------------------')
