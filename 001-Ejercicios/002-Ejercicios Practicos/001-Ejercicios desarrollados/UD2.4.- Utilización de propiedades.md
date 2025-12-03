En este ejercicio se aplica el uso de propiedades y funciones pertenecientes a módulos predeterminados de Python, como es el caso del módulo `math`. 

A partir del contexto propuesto "un aficionado al fútbol que comienza a crear pequeños programas para registrar información", se realiza un ejemplo inicial que permite practicar cómo utilizar valores ya definidos dentro del lenguaje para realizar cálculos precisos. En este caso, se toma como referencia el cálculo de la circunferencia a partir de un radio dado.

---

En primer lugar necesitamos importar la librería `math` y le pondremos el alias de `matematicas` para referirnos a ella en nuestro programa:

```
    import math as matematicas
```

Ahora instanciaremos el radio de nuestra circunferencía:

```
    radio = 2
```

Y ahora utilizaremos la siguiente formula: "2 x pi x r" siendo "pi" el importado de la librería `math` y "r" el radio que declaramos antes:

```
    circunferencia = 2 * matematicas.pi * radio
``` 

Por ultimo el programa mostrará por pantalla el valor de su perímetro:

```
    print(circunferencia)
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
'''
	Calculo circunferencia
	v1.0 Daniel Oliveira Vidal
	Este programa calcula una circunferencía
'''
import math as matematicas

radio = 2

circunferencia = 2 * matematicas.pi * radio

print(circunferencia)
```

**Notas:**

- Es importante poner el nombre que le hemos dado a la librería seguido de un punto y la función que queramos
- El `print` nada más muestra el perimetro de la circunferencía 

---

Este programa muestra de forma sencilla cómo emplear propiedades de módulos integrados en Python, en este caso `math.pi`, para resolver operaciones matemáticas reales. 

A partir de un radio definido, el código calcula la circunferencia utilizando la fórmula correspondiente, reforzando así la comprensión del uso de módulos y del manejo básico de variables y operadores. Este ejercicio sirve como base para desarrollar programas más completos, como el registro de partidos mencionado en el contexto.