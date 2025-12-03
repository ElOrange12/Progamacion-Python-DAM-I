Los `assert` son lo que viene siendo un chivato, estos sirven para cuando algo falla te devuelva un mensaje diciendo en que falló, esto es muy útil para muchas cosas a la hora de hacer pruebas en programas o en cual quier otra cosa.

Por ejemplo pongamos que tenemos un programa que simula un partido de fútbol necesitamos saber si ciertas cosas fallan o no, es decir, si el equipo local tiene que ganar y gana el visitante, que no diga que este no puede ganar.

Vamos a realizar un ejercicio para poner en practica esta técnica

---

Primero declaramos las variables de los goles del equipo local y visitante, para ello lo haremos de la siguiente manera:

```
	goles_local = int(input('Dime los goles del equipo local: '))
	goles_visitante = int(input('Dime los goles del equipo visitante: '))
```

Estos tienen tanto la función `int`, para que sea un número entero sin decimales, y un `input` para que el usuario introduzca los valores de los goles para así probar distintos casos y saber donde falla.

Después de declarar estas dos variables usaremos un `assert` para comprobar un error en concreto que nos a propuesto el enunciado, este va a ser que el equipo visitante no pueda ganar, esto lo realizaremos de la siguiente forma: 

```
	assert goles_local > goles_visitante, 'El equipo visitante no puede ganar'
```

Por último declararemos una variable llamada `partido_tan_traumatico` que almacenará la diferencia de goles entre los dos equipos, para ello lo haremos de la misma manera que la de los goles por el mismo motivo:

```
partido_tan_traumatico = int(input('Dime la diferencia de goles: '))
```

Y utilizaremos otro `assert` exactamente igual que antes pero ahora con otro error distinto, este es que la diferencia no pueda ser tan grande, propuesto tambien por el ejercicio

```
	assert partido_tan_traumatico > 5, 'La diferencia de goles no puede ser tan grande'
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
	'''
		Comprobante de partidos ganados
		v1.0 Daniel Oliveira Vidal
		Este programa te dice si el equipo visitante puede ganar y si la diferencia de goles
	'''

	goles_local = int(input('Dime los goles del equipo local: '))
	goles_visitante = int(input('Dime los goles del equipo visitante: '))

	assert goles_local > goles_visitante, 'El equipo visitante no puede ganar'

	partido_tan_traumatico = int(input('Dime la diferencia de goles: '))

	assert partido_tan_traumatico > 5, 'La diferencia de goles no puede ser tan grande'
```

**NOTAS:**

- El `assert` solo saltará si la condición no se cumple
- El `int` dará error si no es un número entero
- El programa no identifica si el número introducido es un número negativo
- Si los goles de los dos equipo son iguales saltará el `assert` porqué no cumplirá la condición

---

En conclusión el `asser` es una herramienta útil a la hora de comprobar el código o avisar al usuario de que ha salido mal, esto hace mas fácil la programación y ayuda a la solución de errores comunes.

Por lo qué a la hora de hacer nuestro programa o un juego simulado cualquiera es bueno que haya algo que si algo falla te de una explicación de que a pasado y no un error de ejecución cualquiera.
