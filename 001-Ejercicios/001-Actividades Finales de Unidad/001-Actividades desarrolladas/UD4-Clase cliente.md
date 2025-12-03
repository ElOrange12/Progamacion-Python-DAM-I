En este ejercicio se trabaja el concepto de Programación Orientada a Objetos (POO) en Python, utilizando la creación de una clase llamada `Cliente`.

El objetivo principal es almacenar, modificar y acceder a los datos de un cliente mediante el uso de atributos, métodos `set` y `get`.

Este tipo de estructura es muy común en el desarrollo de aplicaciones que gestionan información personal o de negocio, ya que permite mantener los datos encapsulados y acceder a ellos de manera controlada.

La clase Cliente actúa como una plantilla que define cómo deben estructurarse los datos de cada cliente, asegurando que cada objeto creado a partir de ella tenga los mismos campos (nombre, apellidos, correo electrónico y edad).

Además, este código es un ejemplo básico pero muy representativo de cómo se implementan los principios de encapsulación y reutilización del código, dos pilares fundamentales de la POO.

---

Primero creamos la clase `Cliente`:

```
	class Cliente():
```

Despues hacemos el constructor y añadimos diversas propiedades:

```
	def __init__(self, nombre, apellidos, email, edad):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.edad = edad
```

Agregamos `setters` y `getters` a todas las propiedas de la siguiente forma:

```
	def setNombre(self, nuevonombre):
		self.nombre = nuevonombre
	
	def getNombre(self):
		return self.email	
```

Esto para todas las propiedades.

Ahora instanciamos 3 objetos diferentees:

```
	cliente1 = Cliente('Pedro', 'Perez Pozo', 'pedro@pepozo.com', 21)
	cliente2 = Cliente('Patricia', 'Pardo Pineda', 'patricia@papineda.com', 46)
	cliente3 = Cliente('Paco', 'Parker Pinzón', 'paco@papinzon.com', 58)
```

Ahora comprobamos que los `setter` y `getters` funcionen:

```
	cliente1.setEdad(23)
	print(cliente1.getEdad())

	cliente2.setEdad(47)
	print(cliente2.getEdad())

	cliente2.setEdad(61)
	print(cliente2.getEdad())
```

Y ya tenemos el ejercicio resuelto.
---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
'''
	Clase cliente
	v1.0 Daniel Oliveira Vidal
	Este programa almacena mediante una clase, setters y getters cierta información de un cliente
'''
	class Cliente():
		def __init__(self, nombre, apellidos, email, edad):
			self.nombre = nombre
			self.apellidos = apellidos
			self.email = email
			self.edad = edad
		
		def setNombre(self, nuevonombre):
			self.nombre = nuevonombre
			
		def setApellidos(self, nuevosapellidos):
			self.apellidos = nuevosapellidos
			
		def setEmail(self, nuevoemail):
			self.email = nuevoemail
			
		def setEdad(self, nuevaedad):
			self.edad = nuevaedad
			
		def getNombre(self):
			return self.email
			
		def getApellidos(self):
			return self.email
				
		def getEmail(self):
			return self.email
			
		def getEdad(self):
			return self.edad
			
	cliente1 = Cliente('Pedro', 'Perez Pozo', 'pedro@pepozo.com', 21)
	cliente2 = Cliente('Patricia', 'Pardo Pineda', 'patricia@papineda.com', 46)
	cliente3 = Cliente('Paco', 'Parker Pinzón', 'paco@papinzon.com', 58)

	cliente1.setEdad(23)
	print(cliente1.getEdad())

	cliente2.setEdad(47)
	print(cliente2.getEdad())

	cliente2.setEdad(61)
	print(cliente2.getEdad())
```

---

En conclusión, este programa demuestra cómo la clase `Cliente` permite gestionar información de manera ordenada y segura usando métodos `set` y `get` para modificar y consultar los datos de cada instancia.

Gracias a esta estructura, se mejora la organización del código y se evita acceder directamente a los atributos, manteniendo el control sobre los valores almacenados.

Este ejercicio se relaciona directamente con otros contenidos de la unidad, como la creación de objetos, la instanciación de clases y el encapsulamiento de datos, aplicando de forma práctica los fundamentos de la programación orientada a objetos en Python.
