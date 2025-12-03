En este ejercicio se pretende que el alumno comprenda cómo aplicar la programación orientada a objetos en un caso cercano a la vida real, como la gestión de clientes en un negocio relacionado con videojuegos o actividades deportivas. 

Mediante la creación de una clase `Cliente` y la implementación de un pequeño CRUD (Crear y Listar), el programa permite registrar información básica de cada cliente y almacenarla dentro de una lista para su posterior consulta.

---

Primero de todo declararemos nuestra clase, con un constructor para poder añadirle propiedades:

```
    class Cliente():
	def __init__(self):
		self.email = None
		self.nombre = None
		self.direccion = None
```
Ahora instanciaremos un objeto que será `cliente1` y le haremos que el usuario ponga todas las propiedades del cliente y por ultimo mostraremos el cliente:

```
    cliente1 = Cliente()

    email = input('Dime el email del cliente: ')
    nombre = input('Dime el nombre del cliente: ')
    direccion = input('Dime la dirección del cliente: ')

    cliente1.email = email
    cliente1.nombre = nombre
    cliente1.direccion = direccion

    print(cliente1)
```

Ya probado como funciona el objeto crearemos una lista en la que almacenaremos los clientes y empezaremos el `CRUD` con un bucle `while`:

```
    clientes = []

    while True:
```

Dentro del bucle listaremos las opciones que tiene el usuario y le daremos a elegir:

```
    print('1.-Insertar un cliente\n2.-Listar clientes')
	respuesta = int(input('Elige una opción: '))
```

Estas son `Inserta un cliente` y `Listar clientes`, para configurar estas opciones utilizaremos estructuras de control que delimiten que se va a hacer dependiendo de la elección del usuario, siendo la elección 1 la de `Insertar un cliente` y la 2 la de `Listar clientes`:

```
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
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
'''
	Mini CRUD clientes
	v1.0
	Este programa es un ejemplo de un mini CRUD de una lista de clientes
'''

class Cliente():
	def __init__(self):
		self.email = None
		self.nombre = None
		self.direccion = None
		
cliente1 = Cliente()

email = input('Dime el email del cliente: ')
nombre = input('Dime el nombre del cliente: ')
direccion = input('Dime la dirección del cliente: ')

cliente1.email = email
cliente1.nombre = nombre
cliente1.direccion = direccion

print(cliente1)

clientes = []

while True:
	print('1.-Insertar un cliente\n2.-Listar clientes')
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
```

**Notas:**

- El bucle `while` no saldrá a menos que nosotros pongamos una función que lo haga

---

Este mini CRUD demuestra cómo utilizar clases, objetos y listas para gestionar información dentro de una aplicación sencilla.

El alumno aprende a crear instancias, modificar sus atributos y almacenarlas en una colección, simulando un sistema real de administración de clientes.

Este ejercicio sirve como base para futuros desarrollos más avanzados donde se añadan funcionalidades como actualización, eliminación o persistencia de datos.