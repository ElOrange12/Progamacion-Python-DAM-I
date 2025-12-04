Vamos a poner en practica las cosas aprendidas durante las unidades en nuestro examen trimestral, vamos a realizar un CRUD que complemente al examen de BasesDeDatos que hemos hecho anteriormente, en este veremos funciones como bucles, estructuras de selección, objetos importados o definición de funciones.

---

Primero de todo necesitaremos importar el objeto ya creado `mysql.connector` esto nos ayudara a poder conectarnos desde python a la base de datos:

```
	import mysql.connector
```

Añadamos las credenciales necesarias para que el programa pueda interactuar con la base de datos:

```
	conexion = mysql.connector.connect(
		host='localhost',
		user='creadorportafolio',
		password='PortafolioExamen2526$',
		database='portafolioexamen'
	)
	cursor = conexion.cursor()
```

Ahora definamos ciertas funciones que nos ayudarán mas adelante en nuestro `CRUD`.

La primera será de insertar algo en la tabla piezas:

```
	def insertarPieza(titulo, descripcion, imagen, url, id_categoria):
		cursor.execute('''
	  INSERT INTO piezaportafolio
	  VALUES(
		NULL,
		"'''+titulo+'''",
		"'''+descripcion+'''",
		"'''+fecha+'''",
		'''+id_categoria+'''
	  );
	''')
```

En siguiente lugar definamos la función de mostrar cualquier tabla:

```
	def mostrarTabla(tabla):
		cursor.execute('SELECT * FROM '+tabla+';')
		resultado = cursor.fetchall()
		return resultado
```

Y por ultimo definamos eliminar algo de alguna tabla:

```
	def eliminarEnTabla(tabla, identificador):
		cursor.execute('''
		DELETE FROM '''+tabla+'''
		WHERE identificador = '''+identficador+'''
	''')
```

Vemos como estas son funciones simples utilizando el `cursor.execute`, este es el que escribe los comandos de MySQL como se ve en las funciones, en pocas palabras es que hace de intermediario.

Ahora vayamos con el `CRUD`.

Primero de todo pongamos un mensaje de bienvenida:

```
	print('Hola buenas al portafolio')
```

Y acontinuación empezará el `CRUD`, ahora si primero de todo inicializar un bucle `while`.

```
while True:
```

Dentro de este bucle se listarán las opciones que puede hacer el usuario:

```
	print('1.-Insertar en tabla.\n2.-Mostrar tabla\n3.-Actualizar tabla\n4.-Eliminar en tabla.\n5.-Salir')
	respuesta = int(input('Escoge una opción: '))
```

Ahora vayamos con las distintas opciones, para ello utilizaremos estructuras de selección, es decir, `if`/`elif`/`else` para poder diferenciar entre una y otra:

```
	if respuesta == 1:

	elif respuesta == 2:
		
	elif respuesta == 3:

	elif respuesta == 4:		
		
	elif respuesta == 5:
		
	else:
```

En primer lugar la primera opción será insertar una pieza en la tabla `piezaportafolio` de nuestra base de datos, preguntaremos ciertas cosas que luego las incluiremos dentro de la función que creamos anterior mente:

```
	if respuesta == 1:
		titulo = input('Dime el titulo de la pieza: ')
		descripcion = input('Dime la descripción de la pieza: ')
		fecha = input('Dime la fecha de añadido de la pieza: ')
		id_categoria = input('Dime el ID de la categoría: ')
	
		insertarPieza(titulo, descripcion, fecha, id_categoria)
```

Lo siguiente sería mostrar una tabla, esta la haremos de la misma manera que antes solo que utilizando la función `mostrarTabla` en vez de `insertarPieza`:

```
	elif respuesta == 2:
		tabla = input('Qué tabla quieres ver?: ')
		
		resultado = mostrarTabla(tabla)
		for fila in resultado:
			print(fila)
```

Ahora haremos la función de actualizar algo dentro de la base piezas:

```
	elif respuesta == 3:
		print('Vamos a actualizar una pieza de la tabla:')
		
		identificador = input("Introduce el Identificador a actualizar: ")
		titulo = input("Introduce el titulo de la nueva pieza: ")
		descripcion = input("Introduce la descripcion de la nueva pieza: ")
		fecha = input("Introduce la fecha de la nueva pieza: ")
		id_categoria = input('Introduce el ID de la categoría: ')
		cursor.execute('''
		  UPDATE piezaportafolio
		  SET
		  titulo = "'''+titulo+'''",
		  descripcion = "'''+descripcion+'''",
		  fecha = "'''+fecha+'''",
		  id_categoria = input('Introduce el ID de la categoría: '),
		  WHERE Identificador = '''+identificador+'''
		''')
```

Por ultimo dentro del `CRUD` nos queda eliminar algo, para esto será igual que las dos primeras opciones, es decir, con nuestra funcion `eliminarEnTabla` definida anteriormente:

```
	elif respuesta == 4:
		tabla = input('De que tabla quieres borrar: ')
		identificador = input('Dime el idenficador de la cosa que quieres borrar: ')
		
		eliminarEnTabla(tabla, identificador)
```

Ahora como añadido, pongamos dos funciones mas una en `elif == 5:` y otra en `else:`:

```
	elif respuesta == 5:
		print('Adiós')
		print('')
		break
		
	else:
		print('Esa no es una opción correcta.')
		print('')
```

Lo unico que hacen estas funciones es, la primera salir del programa si se selecciona y la segunda si has puesto una opción no valida te lo dice.

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
	'''
		Portafolio
		v1.0 Daniel Oliveira Vidal
		Este programa es un CRUD conectado a una base de datos.
	'''
	import mysql.connector

	conexion = mysql.connector.connect(
		host='localhost',
		user='creadorportafolio',
		password='PortafolioExamen2526$',
		database='portafolioexamen'
	)
	cursor = conexion.cursor()

	def insertarPieza(titulo, descripcion, imagen, url, id_categoria):
		cursor.execute('''
	  INSERT INTO piezaportafolio
	  VALUES(
		NULL,
		"'''+titulo+'''",
		"'''+descripcion+'''",
		"'''+fecha+'''",
		'''+id_categoria+'''
	  );
	''')

	def mostrarTabla(tabla):
		cursor.execute('SELECT * FROM '+tabla+';')
		resultado = cursor.fetchall()
		return resultado
		
	def eliminarEnTabla(tabla, identificador):
		cursor.execute('''
		DELETE FROM '''+tabla+'''
		WHERE identificador = '''+identficador+'''
	''')

	conexion.commit()

	print('')
	print('Hola buenas al portafolio')
	print('')

	while True:
		print('1.-Insertar en tabla.\n2.-Mostrar tabla\n3.-Actualizar tabla\n4.-Eliminar en tabla.\n5.-Salir')
		respuesta = int(input('Escoge una opción: '))
		print('')
		
		if respuesta == 1:
			titulo = input('Dime el titulo de la pieza: ')
			descripcion = input('Dime la descripción de la pieza: ')
			fecha = input('Dime la fecha de añadido de la pieza: ')
			id_categoria = input('Dime el ID de la categoría: ')
		
			insertarPieza(titulo, descripcion, fecha, id_categoria)
			print('')

		elif respuesta == 2:
			tabla = input('Qué tabla quieres ver?: ')
			print('')
			
			resultado = mostrarTabla(tabla)
			for fila in resultado:
				print(fila)
			print('')
			
		elif respuesta == 3:
			print('')
			print('Vamos a actualizar una pieza de la tabla:')
			print('')	
			identificador = input("Introduce el Identificador a actualizar: ")
			titulo = input("Introduce el titulo de la nueva pieza: ")
			descripcion = input("Introduce la descripcion de la nueva pieza: ")
			fecha = input("Introduce la fecha de la nueva pieza: ")
			id_categoria = input('Introduce el ID de la categoría: ')
			cursor.execute('''
			  UPDATE piezas 
			  SET
			  titulo = "'''+titulo+'''",
			  descripcion = "'''+descripcion+'''",
			  fecha = "'''+fecha+'''",
			  WHERE Identificador = '''+identificador+'''
			''')
			print('')

		elif respuesta == 4:
			tabla = input('De que tabla quieres borrar: ')
			identificador = input('Dime el idenficador de la cosa que quieres borrar: ')
			
			eliminarEnTabla(tabla, identificador)		
			
		elif respuesta == 5:
			print('Adiós')
			print('')
			break
			
		else:
			print('Esa no es una opción correcta.')
			print('')
```

**Notas:**

- Los literales de variables que añadamos a los comando de MySQL tiene que ser una cadena virtual
- Importante el uso de los operadores aritmeticos "+" para concatenar los literales de las variables con el DocString.

---

En conclusión podemos ver como así con Python utilizando todo lo que hemos aprendido podemos ver como hemos hecho una manera mucho mas sencilla de añadir, mostrar, actualizar o eliminar cosas.

Hemos hecho que simplemente añadiendo información el programa haga solo todo lo mencionado anteriormente, así alguien que no tiene idea de como utilizar MySQL podría perfectamente utilizar nuestra base de datos, esto hace que no tenga que haber alguien especializado para poder administrar datos.
