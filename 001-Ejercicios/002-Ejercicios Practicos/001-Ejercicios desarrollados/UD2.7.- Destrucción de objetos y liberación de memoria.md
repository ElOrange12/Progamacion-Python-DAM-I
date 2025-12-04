En este ejercicio se plantea una situación en la que, como entrenador de un equipo de fútbol, necesitas organizar a tus jugadores en grupos llamados "cuadras". 

A partir del contexto de un partido lleno de emoción, se utiliza un sencillo programa en Python para aplicar conceptos matemáticos básicos, como la división y el redondeo hacia arriba, haciendo uso del módulo `math`. 

Este programa permite calcular de forma rápida cuántas cuadras son necesarias según el número total de jugadores del equipo.

---

Primero de todo importamos la librería `math` bajo el alias de `matematicas`:

```
    import math as matematicas
```

Después instanciamos las variables necesarias para este ejercicio:

```
    jugadores_del_equipo = 0

    jugadores_x_cuadra = 3
```

Ya con esto preguntamos al usuario cuantos jugadores hay en su equipo utilizando un `int` ya que será un número entero y un `input` para que el usuario pueda ponerlo:

```
    jugadores_del_equipo = int(input('Dime el número de jugadores que hay en tu equipo: '))
```

Por ultimo calcularemos el número de cuadras necesarias para todos los jugadores, esto lo haremos utilizando un división más la función `ceil` de la librería `math`, después de calcularla la mostraremos por pantalla:

```
    numero_de_cuadras = matematicas.ceil(jugadores_del_equipo / jugadores_x_cuadra)

    print('Se necesitan un total de', numero_de_cuadras, 'cuadras.')
```

Esto hará que sea cual sea el resultado de la división aproximará hacia arriba para que ninguna se quede sin cuadra.

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
'''
	Jugadores en cuadras
	v1.0 Daniel Oliveira Vidal
	Este programa divide a jugadores en cuadras y dice cuantas hace falta.
'''
import math as matematicas

jugadores_del_equipo = 0

jugadores_x_cuadra = 3

jugadores_del_equipo = int(input('Dime el número de jugadores que hay en tu equipo: '))

numero_de_cuadras = matematicas.ceil(jugadores_del_equipo / jugadores_x_cuadra)

print('Se necesitan un total de', numero_de_cuadras, 'cuadras.')
```

**Notas:**

- Importante el uso de `int` para los números de jugadores o de cuadras
- Para saber el número de cuadras necesarias es recomendable usar `ceil` para que así aunque se quede alguna medio vacia nadie se quede sin cuadra

---

El programa demuestra cómo Python puede facilitar cálculos prácticos mediante funciones como `ceil()` del módulo `math`, que permite redondear hacia arriba para obtener el número exacto de grupos necesarios. 

Gracias a este ejercicio, se refuerza la comprensión de operaciones matemáticas y del uso de módulos externos, al mismo tiempo que se aprende a aplicar estos conocimientos a situaciones cotidianas y divertidas, como organizar un equipo de fútbol.