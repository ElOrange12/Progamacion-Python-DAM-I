Este programa es una mini aplicación en Python que permite añadir, mostrar y guardar clientes en una lista usando la clase `Cliente` y el módulo `pickle`.

Gracias a la serialización, los datos se guardan en un archivo binario y se mantienen al reiniciar el programa.

El código muestra el uso práctico de la Programación Orientada a Objetos, la gestión de archivos y los menús interactivos.

---

Primero creamos la clase `Cliente` con sus propiedades e importamos `pickle`:

```
	import pickle

	class Cliente():
			def __init__ (self, nombre, apellidos, edad):
				self.nombre = nombre
				self.apellidos = apellidos
				self.edad = edad
```

A continuación creamos una lista llamada `clientes`:

```
	clientes = []
```

Ahora utilizamos un `try-except` para comprobar si hay un archivo existente:

```
	try:
		archivo = open('BaseDeDatosClientes.bin', 'rb')
		clientes = pickle.load(archivo)
	except:
		print('No existe archivo de datos')
```

Comenzemos con el CRUD.

Primero de todo abrimos un bucle `while` y el archivo:

```
	while True:
		archivo = open('BaseDeDatosClientes.bin','wb')
		pickle.dump(clientes, archivo)
		archivo.close()	
```

A continuación le pedimos al usuario que elija una opción entre, añadir cliente, ver clientes o salir:

```
	print('Selecciona una opción:')
	print('1.-Añadir cliente.')
	print('2.-Mostrar clientes.')
	print('3.-Salir')
	
	respuesta = int(input('Escoge una opción: '))
```

Ahora hacemos posibilidades.

Primero la de añadir, lo haremos utilizando una lista y pickle tal que así:

```
	if respuesta == 1:				
		print('Vamos a insertar un cliente')
		nombre = input('Introduce el nombre: ')
		apellidos = input('Indroduce los apellidos: ')
		edad = input('Introduce el edad: ')
		
		clientes.append(Cliente(nombre, apellidos, edad))
```

Continuamos con la opción de mostrar:

```
	elif respuesta == 2:
		identificador = 0
		for nuevocliente in clientes:
			print('Este es el cliente con ID:', identificador)
			print(nuevocliente.nombre, nuevocliente.apellidos, nuevocliente.edad)
			identificador += 1
```

Y por ultimo la de salir, además añadimos una por si pone un opción erronea:

```
	elif respuesta == 3:
		print('Hasta luego')
		print('')
		break
	
	else:
		print('Esa respuesta no es valida')
		print('')
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
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
```

---

En resumen, esta aplicación demuestra cómo combinar clases y archivos binarios para crear un sistema simple de gestión de clientes.

Refuerza conceptos como la persistencia de datos, la creación de objetos y el uso de bucles y condicionales para desarrollar programas funcionales en Python.
