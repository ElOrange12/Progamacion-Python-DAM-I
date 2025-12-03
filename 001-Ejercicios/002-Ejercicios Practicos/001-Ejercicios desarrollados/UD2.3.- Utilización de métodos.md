En el ambito de los videojugos es muy común que los programadores arreglen ciertas cosas que a lo largo del videojuego quedan mucho mejor que como estaban antes de ser arregladas.

Por poner un ejemplo, un poco irreal, a la hora de dar puntuaciones no es muy común ver decimales por lo que los programadores hacen un pequeño fix para así que este no se vea, por ejemplo sería aproximarlo al alza.

Vamos a realizar como podríamos nosotros arreglar esto en python

---

En primer lugar importaremos de la librería `math` la función `ceil`, esta hace que un número se redondee al alza:

```
    from math import ceil
```

Después almacenaremos en una variable una puntuación cualquiera:

```
    puntuacion = 7.2
```

Ahora la redondearemos al alza y la almacenaremos en otra variable, utilizando la función exportada anteriormente:

```
    puntuacion_redondeada = ceil(puntuacion)
```

Ahora mostraremos por pantalla la nueva puntución utilizando un `print`:

```
    print(puntuacion_redondeada)
```

Esto hará que la puntucación final sea distinta a la que teniamos de base y no se mostraran los decimales de esta, es un simple ejemplo de como arreglar un error.

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
    '''
        Redondear puntuaciones
        v1.0 Daniel Oliveira Vidal
        Este programa redondea una puntuaciones al alza utilizando la función "ceil" de la librería "math"
    '''

    from math import ceil

    puntuacion = 7.2

    puntuacion_redondeada = ceil(puntuacion)

    print(puntuacion_redondeada)
```

**Notas:**

- El redonde con la función `ceil` siempre será al alza

---

En conclusión vemos como metodos de librerías de python, que ya vienen predefinidas en este son muy utiles para hacer que nuestros programas esten bien hecho y a nuestro gusto.

Estos nos ayudan a hacer que las respuestas estan a nuestro gusto, arreglar errores, forzar que entra en ciertos sitios...