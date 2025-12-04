En el futbol se puede saber mucho de un jugador durante un partido, esto me recuerda a la POO que podemos hacer creando una clase, en ella podremos almacenar tanto porpiedades o metodos que se pueden hacer con estas.

Vamos a realizar un ejemplo de como podriamos hacerlo

---

Primero creamos la clase:

```
    class Futbolista():
```

Luego definimos sus propiedades, en este caso serán el nombre del jugador, la edad y su posición:

```
    def __init__(self):
            self.nombre = ''
            self.edad = 0 
            self.posicion = ''
```

Después los metodos pedidos.

El primero lo haremos almacenando en otra variable la resta de los años minimos para jubilarse menos la edad que tenga el jugador, después se mostrará por pantalla cuantos años le quedan para jubilarse:

```
    def jubilación(self):
        anyos_para_jubilacion = 65 - self.edad
        print('Le quedan', anyos_para_jubilacion, 'para jubilarse')
```

El segundo simplemente utilizamos una estructura de control para saber si la edad es mayor o menor de 18 años, esta sería la mayoría de edad en la mayoría de paises:

```
    def mayor_edad(self):
        if self.edad >= 18:
            print('Es mayor de edad.')

        else:
            print('No es mayor de edad.')
```

Y por ultimo lo probamos con un jugador cualquiera como podría ser Leo Messi:

```
    jugador1 = Futbolista()
    jugador1.nombre = 'Messi'
    jugador1.edad = 38
    jugador1.posicion = 'Extremo derecho'

    print(jugador1.jubilación())

    jugador1.mayor_edad()
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
    '''
        Clase Futbolista
        v1.0 Daniel Oliveira Vidal
        Este programa crea una clase y en base a una de sus propiedades hace diferentes metodos
    '''

    class Futbolista():
        def __init__(self):
            self.nombre = ''
            self.edad = 0 
            self.posicion = ''
        
        def jubilación(self):
            anyos_para_jubilacion = 65 - self.edad
            print('Le quedan', anyos_para_jubilacion, 'para jubilarse')

        def mayor_edad(self):
            if self.edad >= 18:
                print('Es mayor de edad.')

            else:
                print('No es mayor de edad.')

    jugador1 = Futbolista()
    jugador1.nombre = 'Messi'
    jugador1.edad = 38
    jugador1.posicion = 'Extremo derecho'

    print(jugador1.jubilación())

    jugador1.mayor_edad()
```

**Notas:**

- Si no se introduce la edad no se podrá calcular los años que le quedan para retirarse
- Si no se introduce la edad no se podrá saber si es mayor de edad

---

En conclusión las clases en general nos ayudan a que cierta información este entrelazada entre si y gracias a ello se puedan hacer metodos estaticos los cuales ahorran código y ergonomizan la presentación de este mismo.

Es por todo esto que es importante usarlos como metodo de economización de código.