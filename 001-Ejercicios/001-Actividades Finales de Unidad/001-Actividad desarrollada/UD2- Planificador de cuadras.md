Queremos llevar un registro de los caballos que hay en un cuadra y como estan organizados, es importante tener un registro para tener un orden además de que este almacene el día en el que se hizo el registro.

Vamos a utilizar las cosas aprendidas en la unidad 2, para ello realizaremos un ejercicio que resuelva lo que queremos hacer utilizando metodos y funciones predefinidas de python.

---

Empezamos importando los objetos que utilizaremos a lo largo del ejercicio, esto lo haremos utilizando `import` seguido del nombre de la librería que queramos importar, tal que así:

```
	import datetime as fechas 
	from math import ceil
```

En este caso hemos importado la librería `datetime` y la hemos llamado `fechas` utilizando la función `as` y de la librería `math` solamente hemos importado el metodo `ceil` utilizando la función `from`.

Ahora pediremos al usuario que introduzca las cosas que le pidamos, en este caso todo lo que le pidamos seran número por lo que utilizaremos un `int` más un `input` por lo que todo lo que pidamos seguirá la misma estructura, esta es la siguiente:

```
	caballos = int(input('Dime los caballos que habrá en el establo: '))
```

Primero es el nombre de la variable, seguido de un igual y a continuación las funciones `int` y `input`, dentro del `input` se puede poner una cadena de texto que explique que es lo que pide.

Esto lo realizaremos para pedir las variables de `caballos`, `capacidad_por_cuadra`, `anyo`, `mes` y `dia`.

A continuación validaremos si la respuesta que nos ha dado el usuario es valida utilizando estructuras de control, en este caso `if`.

En el caso de las variables `caballos` y `capacidad_por_cuadra` solo se comprobará si es menor o igual a 0, ya que no se podrá ejecutar el programa, si el número es correcto seguirá con el programa, tal que así:

```
	if caballos <= 0:
		print('Los caballos no pueden ser negativos o no haber ninguno')
		
	else:
```

Después del `else` seguirá el programa.

En el caso de las variables `anyo`, `mes` y `dia`, el `if` dependerá que el año no sea uno que no exista o no haya ocurrido aún, el mes no sea mayor que 12 ni menor que 1 y que el dia no sea mayor que 31 ni menor que 1, los tres usan la misma estructura entre ellos y una parecida a las anteriores variables:

```
	if anyo > 2025 or anyo <= 0:
		print('Ese no es un año valido')
		
	else:
```

Ya teniendo todas las variables las usaremos en distintas cosas, la primera será cuantos caballos caben por cuadra utilizando las variables `caballos` y `capacidad_por_cuadra` ademas de utilizar el metodo `ceil` que importamos antes.

Esto lo haremos dividiendo `caballos` entre `capacidad_por_cuadra` y lo redondearemos al alza usando `ceil`:

```
	cuadras_necesarias = ceil(caballos / capacidad_por_cuadra)
```

Ahora definimos una variable llamada `date` que guarde la fecha de ese dia, esto lo haremos utilizando la libreria `date` de la siguiente manera:

```
	date = fechas.date(anyo, mes, dia)
```

Teniendo la fecha utilizando otra vez la librería `date` comprobaremos de dos formas es que dia de la semana está, utilizaremos `weekday` que da un número del 0 al 6 y `isoweekday` que da un número del 1 al 7.

Por ultimo mostraremos por pantalla todos los datos que tenemos de la siguiente manera:

```
	print('---------------------------------------')
	print('')
	print('Caballos:', caballos)
	print('Capacidad por cuadra:', capacidad_por_cuadra)
	print('Cuadras utilizadas:', cuadras_necesarias)
	print('')
	print('---------------------------------------')
	print('')
	print('Fecha:', date)
	print('Año:', anyo, 'Mes:', mes, 'Día:', dia)
	print('Dia de la semana:', diadelasemana)
	print('Dia de la semana ISO:', isodiadelasemana)
	print('')
	print('---------------------------------------')
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
	'''
		Planificador de cuadras
		v1.0 Daniel Oliveira Vidal
		Este programa hace un registro de una cuadra
	'''
	import datetime as fechas 
	from math import ceil

	caballos = int(input('Dime los caballos que habrá en el establo: '))

	if caballos <= 0:
		print('Los caballos no pueden ser negativos o no haber ninguno')
		
	else:
		capacidad_por_cuadra = int(input('Dime cuantos caballos caben por cuadra: '))

		if capacidad_por_cuadra <= 0:
			print('No pueden no haber ningún caballo o caballos negativos por cuadra')
		
		else:
			anyo = int(input('Dime el año: '))
			
			if anyo > 2025 or anyo <= 0:
				print('Ese no es un año valido')
			
			else:
				mes = int(input('Dime el mes: '))
				if mes > 12 or mes <= 0:
					print('Ese no es un mes valido')
				else:
					dia = int(input('Dime el día: '))
					if dia > 31 or dia <= 0:
						print('Ese no es un dia valido')
					else:
						cuadras_necesarias = ceil(caballos / capacidad_por_cuadra)
						
						date = fechas.date(anyo, mes, dia)

						diadelasemana = date.weekday()
						isodiadelasemana = date.isoweekday()

						print('---------------------------------------')
						print('')
						print('Caballos:', caballos)
						print('Capacidad por cuadra:', capacidad_por_cuadra)
						print('Cuadras utilizadas:', cuadras_necesarias)
						print('')
						print('---------------------------------------')
						print('')
						print('Fecha:', date)
						print('Año:', anyo, 'Mes:', mes, 'Día:', dia)
						print('Dia de la semana:', diadelasemana)
						print('Dia de la semana ISO:', isodiadelasemana)
						print('')
						print('---------------------------------------')
```

**Notas:**

- Se han supuesto intervalos tanto en la variable `anyo` como en `dia`

---

En conclusión vemos como hemos usado lo aprendido en la unidad 2, como importamos librerías y usamos sus metodos esto sirve para cosas que hagas a futuro, debido que nos añaden funciones que nos facilitan el código.
