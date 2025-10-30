Uno de mis hobbies es el fútbol, es por eso que he querido relacionarlo con el mundo de la programación otro de mis hobbies entonces he procedido a hacer un programa el cual cree una clase, la cual sea un equipo de fútbol además de calcular la posición de dos jugadores en el campo y por ultimo una función la cual simule un partido.

--- 

Para empezar definimos importamos de la librería `math` la función `sqrt`, esta hace la raiz cuadrada de lo que le digamos, esta función la usaremos mas adelante a la hora de calcular la distancía del jugador, esto se hace de la siguiente forma:

```
    from math import sqrt
```

Ahora creamos la clase `EquipoFutbol` esta tendrá distintos elementos, como el nombre del equipo, la ciudad de donde son, que jugadores tienen...

Esto lo haremos de la siguiente manera:

```
    class EquipoFutbol():
        def __init__(self):
            self.nombre = ''
            self.ciudad = ''
            self.jugadores = []
```

Ya tenemos la clase hecha vayamos con lo siguiente, queremos calcular la distancia entre dos jugadores en el campo, para esto usaremos el teorema de pitagoras.

Empezaremos definiendo las variables que almacenen la posición del jugador:

```
    pj1 = (2, 1)
    pj2 = (4, 3)
```

Teniendo las posiciones usaremos el teorema de pitagoras para poder calcular la distancia, esto lo haremos de la siguiente manera:

```
    distancia_jugadores = sqrt((pj1[1] - pj1[0])**2 + (pj2[1] - pj2[0])**2)
```

Vale ahora lo que queremos hacer es simular un partido, esto lo haremos definiendo una función la cual se llamará `partidoFutbol` y siendo las entradas de la función dos equipos cualquiera tal que así:

```
    def partidoFutbol(Equipo1, Equipo2):
```

Dentro de la función es recomendable poner un DocString que explique lo que hace la función:

```
    '''
		función partidoFutbol
		Entradas: El nombre de dos equipos
		Salidas: Goles hecho por el primer equipo y el segundo y dice que gana el primero
	'''
```

En primer lugar deberemos definir dos variables que almacenen los goles de los equipos:

```
    goles_equipo_1 = 0
	goles_equipo_2 = 0
```

Ahora vamos con los bucles `for` en los cuales se anotaran goles a los equipos, estos los haremos tal que así:

```
    for i in range(0, 4):
		goles_equipo_1  += 1
	
	for i in range(0, 3):
		goles_equipo_2 += 1
		
```

Por ultimo daremos como ganador a uno de los dos equipos y después haremos que la función devuelva el ganador utilizando un `return`:

```
    ganador = Equipo1
	
	return ganador
```

Teniendo todo esto, ahora toca instanciar dos equipos utilizando la clase `EquipoFutbol` que creamos anteriormente:

```
    equipo_favorito = EquipoFutbol()
    equipo_favorito.nombre = 'FC_Barcelona'
    equipo_favorito.ciudad = 'Barcelona'
    equipo_favorito.jugadores.append('Pedri')

    equipo_rival = EquipoFutbol()
    equipo_rival.nombre = 'Real Vardrid'
    equipo_rival.ciudad = 'Madrid'
    equipo_rival.jugadores.append('Valverde')
```

Y por ultimo poniendo el nombre de cada equipo simularemos el partido con la función definida anteriormente, es decir, `partidoFutbol` será la encargada de simular el partido:

```
    print('El ganador es', partidoFutbol(equipo_favorito.nombre, equipo_rival.nombre))
```

---

A continuación se muestra un ejemplo del código del ejercicio resuelto:

```
    '''
        Equipos de fútbol
        v1.0 Daniel Oliveira Vidal
        Este programa define una clase que se refiere a un equipo de futbol, calcula la distancia entre dos jugadores, hace una función de simulación de partido y por ultimo hace instancias de dos equipos y simula el partido con estos dos.
    '''
    from math import sqrt

    class EquipoFutbol():
        def __init__(self):
            self.nombre = ''
            self.ciudad = ''
            self.jugadores = []
            
    pj1 = (2, 1)
    pj2 = (4, 3)

    distancia_jugadores = sqrt((pj1[1] - pj1[0])**2 + (pj2[1] - pj2[0])**2)

    def partidoFutbol(Equipo1, Equipo2):
        '''
            función partidoFutbol
            Entradas: El nombre de dos equipos
            Salidas: Goles hecho por el primer equipo y el segundo y dice que gana el primero
        '''
        goles_equipo_1 = 0
        goles_equipo_2 = 0
        
        for i in range(0, 4):
            goles_equipo_1  += 1
        
        print('El', Equipo1, 'a marcado', goles_equipo_1, 'goles')
        
        for i in range(0, 3):
            goles_equipo_2 += 1
            
        print('El', Equipo2, 'a marcado', goles_equipo_2, 'goles')
            
        ganador = Equipo1
        
        return ganador
        
    equipo_favorito = EquipoFutbol()
    equipo_favorito.nombre = 'FC_Barcelona'
    equipo_favorito.ciudad = 'Barcelona'
    equipo_favorito.jugadores.append('Pedri')

    equipo_rival = EquipoFutbol()
    equipo_rival.nombre = 'Real Vardrid'
    equipo_rival.ciudad = 'Madrid'
    equipo_rival.jugadores.append('Valverde')

    print('El ganador es', partidoFutbol(equipo_favorito.nombre, equipo_rival.nombre))
```

**Notas:**

- En los atributos de la clase fallará si introducimos un literal númerico en el nombre del equipo o de la ciudad
- La distancía entre dos jugadores la predefinimos nosotros será siempre la misma
- El ganador de partido siempre será el primer equipo y siempre seran los mismos goles

---

En conclusión los objetos predefinidos en python y los que nosotros creamos son muy parecidos haciendo que una simple función haga lo que harian varias lineas de código.

En el mundo del fútbol el concepto de un objeto puede ser a como llames a un movimiento que haces con el balón o una serie de acciones que para ambitos practicos es mas facil ponerle un simple nombre y no nombrar todos los movimientos