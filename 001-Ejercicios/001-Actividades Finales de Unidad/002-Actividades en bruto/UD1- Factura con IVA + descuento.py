'''
	Factura con IVA descuento
	v1.0 Daniel Oliveira Vidal
	Este programa imprime por pantalla tickets aplicando el IVA y un descuento a precios brutos mayores o iguales a 50€
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
	aplica_descuento = True

########## Confirmamos que no tiene descuento ##########
else:
	aplica_descuento = False

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
