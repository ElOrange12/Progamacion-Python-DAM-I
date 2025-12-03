Me gusta mucho tener información de los partidos que veo por lo qué me gustaría tener un programa que me dijerá exactamente lo que quiero saber de un partido.

Pero bueno para eso somos programadores y utilizando clases y objetos podemos hacer eso, vamos a realizar un simple ejercicio como ejemplo a este problema que tenemos.

---

En primer lugar deberemos crear la clase, a esta la llamaremos PartidoFutbol:

```
    class PartidoFutbol():
```

Dentro de esta deberemos añadirle dos atributos que sean los nombres de los equipos y un metodo que imprima por pantalla los equipos que jugaron el partido definido, esto lo haremos de la siguiente manera:

```
    def __init__(self):
        self.nombre_equipo_local = ''
        self.nombre_equipo_visitante = ''

    def mostrar_info(self):
        print('El partido lo jugaron los equipos:', self.nombre_equipo_local, 'y', self.nombre_equipo_visitante)
```

Esto lo que hará es almacenar dos nombres que luego serán los que hayan jugado el partido.

Ahora por ultimo solo falta hacer un ejemplo instanciando un partido de fútbol, en este caso "El Clasico" que se juega entre el FC Barcelona y el Real Madrid, primero instanciaremos una variable para que sea igual a la clase que hemos creado y después instanciaremos los nombres de los equipos:

```
    clasico = PartidoFutbol()
    clasico.nombre_equipo_local = 'FC Barcelona'
    clasico.nombre_equipo_visitante = 'Real Madrid'
```
Después de esto llamaremos al metodo que muestre quien jugo cada el partido:

```
    clasico.mostrar_info()
```

Por ultimo pondremos otro ejemplo, pero en este caso entre la Juventus y el Manchester United:

```
    semis_champions = PartidoFutbol()
    semis_champions.nombre_equipo_local = 'Manchester United'
    semis_champions.nombre_equipo_visitante = 'Juventus'
    semis_champions.mostrar_info()
```

---

A continuación se muestra un ejemplo de código del ejercio resuelto:

```
    '''
        Clase PartidoFutbol
        v1.0 Daniel Oliveria Vidal
        Este programa crea una clase, con la cual se puede instanciar dos nombre de equipos de fútbol y llamar a un metodo que te diga quien jugo ese partido.
    '''

    class PartidoFutbol():
        def __init__(self):
            self.nombre_equipo_local = ''
            self.nombre_equipo_visitante = ''

        def mostrar_info(self):
            print('El partido lo jugaron los equipos:', self.nombre_equipo_local, 'y', self.nombre_equipo_visitante)

    clasico = PartidoFutbol()
    clasico.nombre_equipo_local = 'FC Barcelona'
    clasico.nombre_equipo_visitante = 'Real Madrid'
    clasico.mostrar_info()

    semis_champions = PartidoFutbol()
    semis_champions.nombre_equipo_local = 'Manchester United'
    semis_champions.nombre_equipo_visitante = 'Juventus'
    semis_champions.mostrar_info()
```

**Notas:**
- Si al instanciar los nombres del equipo introducimos un literal númerico fallará
- Si no se instancian los dos nombre de los equipos el programa dará error

---

En conclusión podemos ver como la programación orientada a objetos hace que nosotros a algo podamos hacer que haga ciertas cosas facilitando y simplificando funciones basicas o que ocupen código de mas, además que se almacene todo en el mismo objeto y puede quedar todo relacionado.