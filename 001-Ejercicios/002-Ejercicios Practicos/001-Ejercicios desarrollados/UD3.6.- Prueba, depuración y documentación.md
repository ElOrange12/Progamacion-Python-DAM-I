A la hora de ejucutar funciones, al ser un caja negra, no sabemos que pasa dentro entonces en una buena practica el documentar las respuestas o errores que puede dar la función, esto hace que el usuario el cual importa la librería sepa que pasa.

Para ello haremos una función la cual puede dar varios errores, en este casa haremos una función que haga la raiz de un número y dependiendo del literal devolverá distintos resultados.

---

Vamos a empezar definiendo la función, hay que recordar que ha estas se les nombra en camellCase, para definirla lo haremos tal que así:

```
	def raizSegura(numero):
```

A continuación es recomendable y de buenas practicas poner un "docstring" que documente como se llama la función, las entradas que tendrá y que salidas tiene, esto es simplemente poniendo tres `'` seguidas antes y después del texto, esto se hará de la siguiente manera:

```
	'''
		Función raizSegura
		Entradas: Radicando que se espera que se un número
		Salida: El resultado dependerá en el literal que entra a la función:
			1.- Si es numérico ---> Devolverá la raíz del número
			2.- Si se puede convertir a numérico ---> Devolverá la raíz del número
			3.- Si es numérico pero negativo ---> Devolverá 0
			4.- Si no se puede convertir a numérico ---> Devolverá 0 
	'''
```

Vayamos ahora con la función en sí, lo primero que debemos hacer para calcular la raiz de algo es exportar de la librería math la función `sqrt` tal que así:

```
	from math import sqrt
```

Teniendo ya como hacer la raiz empezemos a operar, en primer lugar si el literal que entra es un `int` o un `float`, para comprobar esto utilazeromos una estructura de selección `if` y `else` de la siguiente manera:

```
	if isinstance(numero, (int, float)):
```

Si este es una cadena se irá al `else`.

Después dentro de este dependera de si el número es positivo o negativo, para ello volveremos a usar la estructuras de selección de esta manera:

```
	if numero >= 0:
	
	else:
```

Ahora dentro del positivo calculará la raiz y la devolverá usando un `return` pero dentro del negativo saltará un `assert` diciendo que el numero no puede ser negativo y devolverá 0, esto lo hará de la siguiente manera:

```
	if numero >= 0:
		raiz_numero = sqrt(numero)
		return raiz_numero
	else:
		assert numero >= 0, 'El número es negativo'
		return 0
```

A continuación de esto volvemos atrás para el caso de que no sea una cadena es decir el `else` que no rellenamos antes, en este habrá un `try-except` en el `try` el programa probará si la cadena se puede convertir a númerico, una vez comprobado hará la raiz del número que salga de la siguiente forma:

```
	try:
		numero = float(numero)
		raiz_numero = sqrt(numero)
		return raiz_numero		
```

Y en el `except` simplemente habrá un asser que avise que el literal no es númerico y devolverá 0, tal que así:

```
	except:
		return 0
		assert isinstance(numero, (float)), 'No se ha convertido a numérico'
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
	def raizSegura(numero):
		'''
			Función raizSegura
			Entradas: Radicando que se espera que se un número
			Salida: El resultado dependerá en el literal que entra a la función:
				1.- Si es numérico ---> Devolverá la raíz del número
				2.- Si se puede convertir a numérico ---> Devolverá la raíz del número
				3.- Si es numérico pero negativo ---> Devolverá 0
				4.- Si no se puede convertir a numérico ---> Devolverá 0 
		'''
		from math import sqrt

		if isinstance(numero, (int, float)):
			if numero >= 0:
				raiz_numero = sqrt(numero)
				return raiz_numero
			else:
				assert numero >= 0, 'El número es negativo'
				return 0
				
		else:
			try:
				numero = float(numero)
				raiz_numero = sqrt(numero)
				return raiz_numero
				
			except:
				return 0
				assert isinstance(numero, (float)), 'No se ha convertido a numérico'
```

**NOTAS:**

- Los assert no funcionan como prints por lo que dará el error pero no devolverá 0, el enunciado me incita a ponerlo.
- No se puede no exportar sqrt, sino no podría hacer la raiz de algo.

---

En conclusión la depuración el código ayuda a que sepamos por donde va la traza de este mismo y podamos identificar errores con mas precisión ahorrandonos mucho tiempo y evitando otros errores a la hora de arreglarlo.
