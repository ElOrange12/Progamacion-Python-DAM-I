Queremos realizar una operación pero al dividir surge un error, dividimos por cero y no nos da un valor si no que un error ¿que ha pasado?.

Aquí nos damos cuenta de las excepciones, estas pueden surgir a la hora de hacer una interacción, por lo qué como somos programadores vemos este problema y lo hacemos un ejercicio y lo intentaremos arreglar.

---

Para empezar anunciamos que vamos ha hacer utilizando un simple `print`, en este caso vamos a realizar una división por lo qué es lo que pondremos en el literal del `print`, es decir:

```
	print('Vamos a hacer una división')
```

Vamos a realizar la división para ello necesitamos un divisor y un dividendo, entonces necesitaremos preguntárselo al usuario para ello utilizaremos un `input` además de un `float` por qué la respuesta se tratara de número y al no saber si llevará decimales o no le ponemos un `float`, todo esto se almacenará en variables, es decir:

```
	a = float(input('Dime el dividendo; '))
	b = float(input('Dime el divisor: '))
```

Ahora viene el problema, al dividir ¿que pasa si el divisor es 0?, pues para ello utilizaremos la función try-except, esta el la encargada de manejar excepciones, para utilizar esta estructura se hace de la siguiente manera: se pone `try:` y en la siguiente linea, poniendo un sangrado, se pone lo que se quiere intentar ejecutar, en este caso la división, después se pone `except`, este sin sangrado, y a continuación de este un `print` con la explicación del error, este `print` si va con sangrado, es decir:

```
	try:
		print(a / b)
	except:
		print('No se puede dividir entre 0')
```

Por lo que primero se intentará ejecutar el apartado `try` y en el caso de que de un error se ejecutara el apartado `except`.

Por ultimo añadimos al final del programa un `print` el cual se ejecute después del `try-except` para comprobar que se sigue ejecutando código después de este.

---

A continuación se muestra un ejemplo de código del ejercicio resuelto: 

```
	'''
		Division con fix de DIVISION x 0
		v1.0 Daniel Oliveira Vidal
		Este programa prueba ha hacer una división, si esta falla muestra un error y continua.
	'''

	print('Vamos a hacer una división')

	a = float(input('Dime el dividendo; '))
	b = float(input('Dime el divisor: '))

	try:
		print(a / b)
	except:
		print('No se puede dividir entre 0')
		
	print('Hemos terminado de operar')
```

---

En conclusión vemos como esto es aplicable a cualquier error, esta estructura trata de dar una opción la cual si o si se ejecute después de que una anterior falle, esto ayuda a que el programa continué sin problemas.
