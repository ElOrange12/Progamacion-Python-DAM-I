Queremos hacernos ticket de una compra que hemos hecho en una tienda, además si hacemos una compra mayor o igual a 50€ nos aplican un descuento, pero como somos programadores vamos aplicar nuestros conocimientos en variables y estructuras de selección para hacer que un programa nos lo hago solo.

Esto se utiliza básicamente en la automatización de todo lo que nos rodea, simplemente por el fin de ahorrarnos trabajo a posteriori

Por lo que vamos a poner el ejercicio propuesto en marcha.

---

Comenzamos pidiéndole el nombre del cliente y el precio bruto del ticket al usuario, para esto se utiliza la función `input`, es decir:

```
	nombre_cliente = input('Dime el nombre del cliente: ')
```

Pero en el caso del precio bruto al ser un número y además decimal deberemos utilizar la función `float`, esta convierte el literal de la variable a un número decimal, esto lo podemos hacer de dos maneras:

_Extensa_
```
	precio_bruto = input('Dime el precio bruto del producto: ')
	precio_bruto = float(precio_bruto)
```

_Compacta_
```
	precio_bruto = float(input('Dime el precio bruto del producto: '))
```

En este ejercicio nos hemos decantado por la compacta.

A continuación declaramos las constantes de `IVA` y `DESCUENTO`, debido que en python no existe diferencia entre una variable y una constante para diferenciarlas escribimos las constantes totalmente en mayúsculas de la siguiente manera:

```
	IVA = 0.21
	DESCUENTO = 10
```

Ya teniendo todas las variables que necesitamos procederemos a calcular el subtotal con IVA del ticket.

Para hacer esto calcularemos el precio añadido al aplicar el IVA, esto se realizará multiplicando el precio bruto por el IVA y a su vez el resultado de este se le sumará al propio precio bruto, para esto utilizamos operadores aritméticos como el `+` y `*`, además que el resultado de estas operaciones se almacenará en variables es decir:

```
	iva_aplicado = precio_bruto * IVA
	subtotal_con_iva = precio_bruto + iva_aplicado
```

Ahora para comprobar si se aplica el descuento utilizaremos las estructuras de selección `if`/`else`, estas las utilizamos para atribuir condiciones.

Utilizando estas estructuras atribuimos que si la variable `precio_bruto` es mayor o igual (`>=`) que 50 se aplicará el descuento, para almacenar si se aplica o no el descuento utilizamos una variable booleana en este caso `aplica_descuento`, en la cual sera `True` si se aplica o `False` si no, es decir:

```
	if precio_bruto >= 50:
		aplica_descuento = True
		
	else:
		aplica_descuento = False
```

Entonces si la condición de que se aplica el descuento se ejecuta calcularemos el subtotal con el descuento aplicado, esto lo haremos utilizando de nuevo los operadores aritméticos, en este caso el `-`, y almacenándolo en otra variable, para calcular este subtotal le restaremos al subtotal con el IVA atribuido el descuento que declaramos antes, es decir:

```
	if precio_bruto >= 50:
		subtotal_con_descuento = subtotal_con_iva - DESCUENTO
```

Por ultimo tenemos que imprimir un ticket con el desglose de todo lo calculado anteriormente, para imprimir por pantalla utilizaremos `print` y como tenemos una variable la cual almacena si se aplica o no el descuento la utilizaremos junto a las estructuras de repetición.

Habrá dos posibles tickets, se imprimirá uno o el otro dependiendo de si se aplica descuento o no y esto lo haremos con lo explicado anteriormente, el cambio que se da en los dos tickets es el `TOTAL` y el `DESCUENTO`, este ultimo será 0 si no se aplica y 10 si se aplica, es decir:

```
	if aplica_descuento == False:
		print('--------------------------------')
		print('Nombre:', nombre_cliente)
		print('--------------------------------')
		print('Precio bruto:', precio_bruto)
		print('IVA aplicado:', iva_aplicado)
		print('Descuento aplicado: 0')
		print('')
		print('TOTAL:', subtotal_con_iva)
		print('--------------------------------')

	else:
		print('--------------------------------')
		print('Nombre:', nombre_cliente)
		print('--------------------------------')
		print('Precio bruto:', precio_bruto)
		print('IVA aplicado:', iva_aplicado)
		print('Descuento aplicado:', DESCUENTO )
		print('')
		print('TOTAL:', subtotal_con_descuento)
		print('--------------------------------')
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
	'''
		Factura con IVA descuento
		v1.0 Daniel Oliveira Vidal
		Este programa imprime por pantalla tickets aplicando el IVA y un descuento a precios mayores o iguales a 50€.
	'''

	#################### Pedimos datos iniciales ####################
	nombre_cliente = input('Dime el nombre del cliente: ')
	precio_bruto = float(input('Dime el precio bruto del producto: '))

	#################### Declaramos las constantes ####################
	IVA = 0.21
	DESCUENTO = 10

	############################## Calculamos el precio sin descuento ##############################
	iva_aplicado = precio_bruto * IVA
	subtotal_con_iva = precio_bruto + iva_aplicado

	########## Calculamos descuento ##########
	if precio_bruto >= 50:
		subtotal_con_descuento = subtotal_con_iva - DESCUENTO
		aplica_descuento = True		# Variable booleana

	########## Confirmamos que no tiene descuento ##########
	else:
		aplica_descuento = False	# Variable booleana

	############################## Imprimimos el ticket ##############################

	########## Sin descuento ##########
	if aplica_descuento == False:
		print('--------------------------------')
		print('Nombre:', nombre_cliente)
		print('--------------------------------')
		print('Precio bruto:', precio_bruto)
		print('IVA aplicado:', iva_aplicado)
		print('Descuento aplicado: 0')
		print('')
		print('TOTAL:', subtotal_con_iva)
		print('--------------------------------')

	########## Con descuento ##########
	else:
		print('--------------------------------')
		print('Nombre:', nombre_cliente)
		print('--------------------------------')
		print('Precio bruto:', precio_bruto)
		print('IVA aplicado:', iva_aplicado)
		print('Descuento aplicado:', DESCUENTO )
		print('')
		print('TOTAL:', subtotal_con_descuento)
		print('--------------------------------')
```

**NOTAS:**

- Después de una función de selección debe haber un sangrado para que se ejecute el código si se da la condición.
- Las variables se escriben en minúsculas y las constantes en mayúsculas, para que haya una distinción visual.

---

En conclusión vemos como todo esto nos sirve para darnos cuenta de como un ejemplo tan real fuera del ámbito en el que nos encontramos se puede resolver con aplicaciones sencillas y lineas de código, esto hace que veamos como aprender a programar no solo va a servir para diseñar juegos, si no que es una manera de aplicar la lógica a problemas simples y cotidianos de forma que se resuelvan siempre igual.
