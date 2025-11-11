Para entreternos haremos un juego de adivinar un número, para ello utilizaremos las cosas aprendidas en la unidad 3.

Esto son bucles, estructuras de selección, estructuras de control...

Estas nos ayudarán a hacer el ejercicio

---

Para empezar importaremos la librería `random` de python:

```
	import random
```

Ahora definiremos las variables principales del programa, es decir, los intentos, la respuesta vacía y el número secreto, para el número secreto utilizaremos un metodo de la librería `random`, esto lo haremos de la siguiente manera:

```
intentos = 6
numero = random.randint(1, 50)
respuesta = ''
```

Empezamos un bucle `while` el cual solo acabe si los intentos son 0 o si acierta el número secreto, tal que así:

```
	while respuesta != numero or intentos == 0:
```

Empezamos diciendo si los intentos son 0 se acabe el bucle, tal que así:

```
	if intentos == 0:
		break
```

Sino empezará todo lo demás.

Lo primero de todo será preguntar que número cree que es:

```
	respuesta = input('Dime un número del 1 al 50: ')
```

A continuación empezaremos otro bucle que este activo infinitamente a menos que lo rompamos es decir un `while True`:

Dentro de este habrá un `try-except`, en el `try` se intentará convertir a entero la respuesta del usuario:

```
	respuesta = int(respuesta)
```

Después de trasformarlo a entero utilizaremos estructuras de control para comprobar distintos casos

Primero de todo comprobar que el número que dijo el usuario esta dentro del rango:

```
	if respuesta < 1 or respuesta > 50:
		print('El numero esta fuera de rango')
```

Si esta fuera del rango la respuesta no restará un intento solo volverá a preguntar pero si esta dentro del rango habrán otros casos.

Primero de todo que la respuesta sea distinta al número secreto si no el programa avisará y restará un intento, aparte si la respuesta es mayor o menor que el número secreto el programa tambien lo indicará y por ultimo si el usuario fallará tres veces le dirá si el número secreto es par o impar,
por ultimo un ultimo caso es que se quede sin intentos entonces, le dirá lo anterior:

```
	if respuesta != numero:
		print('Ese no es el número que estoy pensando.')
		intentos -= 1
		
		if respuesta > numero:
			print('El que me has dicho es demasiado alto.')
			print('')
			
		elif respuesta < numero:
			print('El que me has dicho es demasiado bajo.')
			print('')
		
		if intentos == 3:
			prueba_paridad = numero % 2
			if prueba_paridad == 0:
				print('El número secreto es par.')
				print('')
				
			else:
				print('El número secreto es impar.')
				print('')
				
		if intentos == 0:
			print('Te quedas sin intentos lo siento, el número era el', numero)
			print('')
			break
		
		else:
			print('Te quedan', intentos, 'intentos.')
			print('')
			break
		
	else:
		print('Correcto el número era el', numero, '.')
		print('')
		break
```

Ahora en el `except` te dirá si el número que introduciste no es valido, es decir, que sea un `float` o que no sea un literal numérico:

```
	try:
		respuesta = float(respuesta)
		assert isinstance(respuesta, (int, float))
		print('Ese no es un número valido')
		print('')
		break
		
	except:
		print('Ese no es un caracter valido')
		print('')
		break
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
```

---

En conclusión todo lo aprendido en la unidad 3 nos sirve para la solución de problemas a nuestro antojo y que simplemente el programa fallé

