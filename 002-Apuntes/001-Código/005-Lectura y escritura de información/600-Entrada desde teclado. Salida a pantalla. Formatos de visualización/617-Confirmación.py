class Cliente():
	def __init__():
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		
print('##### Gestion de clientes v0.1 #####')
print('##### Daniel Oliveira Vidal #####')

clientes = []

while True:
	print('Escoge una opción:')
	print('1.- Insertar un cliente')
	print('2.- Listar clientes')
	print('3.- Actualizar un cliente')
	print('4.- Eliminar un cliente')
	opcion = int(input('Escoge una opcion: '))
	
	if opcion == 1:
		nombre = input('Introduce el nombre: ')
		apellidos = input('Indroduce los apellidos: ')
		email = input('Introduce el email: ')
		clientes.append(Cliente(nombre, apellidos, email))
	elif opcion == 2:
		identificador = 0
		for cliente in clientes:
			print('Este es el cliente con ID:', identificador)
			print(cliente.nombre, cliente.apellidos, cliente.email)
			identificador += 1
	elif opcion == 3:
		identifcador = int(input('Introduce el id para modificar: '))
		nombre = input('Introduce el nombre: ')
		apellidos = input('Indroduce los apellidos: ')
		email = input('Introduce el email: ')
		clientes[identificador].nombre = nombre
		clientes[identificador].apellidos = apellidos
		clientes[identificador].email = email
	elif opcion == 4:	
		identifcador = int(input('Introduce el id para eliminar: '))
		confirmacion = input('¿Estás seguro? (S/n): ')
		if confirmacion == 'S':
			clientes.splice(identificador, 1)
		elif confirmacion == 'n':
			print('Cancelado')
		else:
			print('Opción no válida')
		
	
		
