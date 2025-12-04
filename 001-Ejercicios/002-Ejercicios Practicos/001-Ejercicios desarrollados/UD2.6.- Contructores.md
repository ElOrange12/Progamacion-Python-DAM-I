En este ejercicio se trabaja con el módulo `datetime` de Python para aprender a manejar fechas de una forma sencilla y práctica. Partiendo del contexto de alguien que, mientras jugaba al fútbol en el parque, decidió aprender a calcular qué día de la semana es hoy y cuántos días faltan hasta su próximo cumpleaños, el programa utiliza funciones básicas del módulo para crear fechas, compararlas y obtener intervalos de tiempo.

Este ejemplo sirve como una primera aproximación al uso de fechas reales dentro de programas útiles en el día a día.

---

Primero de todo importamos la librería `datetime` bajo el alias de `fechas`:

```
    import datetime as fechas
```

A continuación declaramos una variable en la cual almacenaremos que día es hoy:

```
    fechahoy = fechas.date(2025-11-14)
```

Ya teniendo la variable, la mostraremos por pantalla:

```
    print(fechahoy)    
```

Ahora comprobaremos que dia de la semana es, siendo el 0 el lunes y el 6 el domingo, después de comprobarlo lo mostraremos por pantalla:

```
    diadelasemana = fechas.weekday()
    print(diadelasemana)
```

Como ultima funcionalidad haremos que calcule el tiempo que queda para mi cumpleaños, primero deberemos declarar dos variables una que almacene mi edad y otra el día de mi cumpleaños:

```
    mi_edad = 18

    cumple = fechas.date(2007, 4, 12)
```

Ahora comprobemos si el cumple ya a pasado:

```
    cumple_este_anyo = cumple.replace(year=fechahoy.year)
```

Ahora mediante estructuras de control haremos lo siguientes casos:

```
    if cumple_este_anyo < fechahoy:
        cumple_proximo = cumple_este_anyo.replace(year=fechahoy.year + 1)
    else:
        cumple_proximo = cumple_este_anyo
```

Mostraremos cuando es mi proximo cumpleaños:

```
    print('Próximo cumpleaños:', cumple_proximo)
```

Y por ultimo calcularemos los dias restantes que quedan y los mostraremos por pantalla:

```
    dias_faltan = (cumple_proximo - fechahoy).days
    print('Días hasta tu próximo cumple:', dias_faltan)
```

---

```
'''
	Fechas y dias
	v1.0 Daniel Oliveira Vidal
	Este programa muestra distintos datos sobre el dia de hoy y mi cumpleaños
'''
import datetime as fechas

fechahoy = fechas.date(2025-11-14)

print(fechahoy)

diadelasemana = fechas.weekday()
print(diadelasemana)

mi_edad = 18

cumple = fechas.date(2007, 4, 12)

cumple_este_anyo = cumple.replace(year=fechahoy.year)

if cumple_este_anyo < fechahoy:
	cumple_proximo = cumple_este_anyo.replace(year=fechahoy.year + 1)
else:
	cumple_proximo = cumple_este_anyo
	
print('Próximo cumpleaños:', cumple_proximo)

dias_faltan = (cumple_proximo - fechahoy).days
print('Días hasta tu próximo cumple:', dias_faltan)
```

**Notas:**

- Es importante poner el nombre que le hemos dado a la librería seguido de un punto y la función que queramos
- El programa solo calculará en base al año definido por nosotros en este caso mi cumpleaños

---

Este programa demuestra cómo Python permite manipular fechas de forma clara mediante el módulo `datetime`, mostrando el día actual, calculando la fecha del próximo cumpleaños y determinando cuántos días faltan para que llegue. 

Al realizar comparaciones y operaciones entre fechas, se refuerza la comprensión del manejo de objetos tipo `date` y sus propiedades. Este ejercicio sirve como una base sólida para crear aplicaciones más complejas que dependan del tiempo y las fechas.