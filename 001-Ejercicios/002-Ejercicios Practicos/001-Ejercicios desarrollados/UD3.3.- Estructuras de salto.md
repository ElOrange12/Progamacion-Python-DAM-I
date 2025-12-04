Queremos trabajar con funciones, estas las utilizamos para un ahorro de trabajo y no tener que poner acciones todo el rato, esto hace que economicemos el código, en relación con mi hobby tenemos un ejemplo de una función que le suma puntos a jugadores en un torneo de videojuegos, esto es una herramienta muy útil para así ser mas rápidos en un recuento de puntos.

---

El programa comienza definiendo la función utilizando la palabra reservada `def`,después el nombre de la función en formato camellCase seguido de unos paréntesis los cuales tengan dentro las variables que se van a utilizar dentro de la función.

Esto lo haremos de la siguiente forma:

```
def sumaPuntos(puntos_jugador1, puntos_jugador2):
```

Después haremos el código de la función, este deberá ir sangrado.

Para hacer la función `sumarPuntos`, haremos que dos variables (`puntos_jugador1` y `puntos_jugador2`) se sumen y se guarden en otra variable (`puntos_totales`), esto se hará de la siguiente manera:

```
puntos_totales = puntos_jugador1 + puntos_jugador2
```

A continuación de eso para que la función devuelva lo que queremos, utilizaremos la palabra reservada `return`, esta devolverá la variable `puntos_totales` de la siguiente manera:

```
return puntos_totales
```

Por último para comprobar que la función funciona utilizaremos un `print` con dos atributos, que estos serán número, que se sumaran y dará el resultado de estos:

```
print(sumaPuntos(2, 1))
```

Este último `print` ya no esta sangrado debido que no pertenece a la función.

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
'''
	Función sumaPuntos
	v1.0 Daniel Oliveira Vidal
	Este programa tiene una función la cual le suma puntos a jugadores
'''

def sumaPuntos(puntos_jugador1, puntos_jugador2):
	
	puntos_totales = puntos_jugador1 + puntos_jugador2
	return puntos_totales
	
print(sumaPuntos(2, 1))
```

**Notas: **

- Las funciones deben estar escritas en camellCase, como buenas practicas
- Hay que utilizar un `return` para que se devuelva algo

---

La relación que tiene esta actividad con mi hobby, tiene que ver por ejemplo a como el definir funciones es muy útil en muchos aspectos en el cuál se repite las mismas acciones muchas veces, es por esto que al definirlas ahorramos en código.
