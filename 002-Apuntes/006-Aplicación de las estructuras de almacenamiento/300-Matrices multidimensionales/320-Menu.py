import pickle

agenda = []

while True:
	print('Seleciona una opción:\n1.-Insertar un registro\n2.-Leer registros\n3.-Guardar registros')
	opcion = int(input('Opción escogida: '))

	if opcion == 1:	
		# Insertar
		nombre = input('Dime tu nombre: ')
		apellidos = input('Dime tus apellidos: ')
		email = input('Dime tu email: ')
		telefono = input('Dime tu teléfono: ')
		agenda.append([nombre, apellidos, email, telefono])
	
	elif opcion == 2:
		#Imprimir
		print(agenda)
	
	elif opcion == 3:
		#Guardar
		archivo = open('agenda.bin', 'wb')
		pickle.dump(agenda, archivo)
		archivo.close()

