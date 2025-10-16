'''
	Impresora de tickets
	v1.0 Daniel Oliveira Vidal
'''

############### Pedimos el nombre del cliente ###############
cliente_nombre = input('Dime el nombre del cliente: ')

############### Pedimos la edad del cliente ###############
edad = int(input('Dime la edad del cliente: '))

##### Comprobamos que tenga edad positiva #####
if edad < 0:
	print('El cliente no puede tener edad negativa.')

##### Comprobamos que sea mayor de edad #####
elif edad >= 0 and edad < 18:
	print('No se puede imprimir el ticket porqué es menor de edad.')
		
else:
	
	############### Pedimos la base imponible del ticket ###############
	base_imponible = float(input('Dime la base imponible del producto: '))
	
	##### Comprobamos que la base no sea negativa o nula #####
	if base_imponible <= 0:
		print('La base imponible no pueder ser negativa o nula.')
		
	else:
		
		############### Declaramos el IVA ###############
		IVA = 0.21		# IVA = 21%
		
		############### Comprobamos el descuento que se le atribuye ###############
		if base_imponible < 100:
			descuento_hecho = 0
			descuento = 0	
			
		elif base_imponible >= 100 and base_imponible < 199:
			descuento_hecho = 5
			descuento = 0.05
			
		else:
			descuento_hecho = 10
			descuento = 0.1
		
		############### Calculamos el TOTAL y su desglose ###############
		importe_descuento = base_imponible * descuento
		base_tras_descuento = base_imponible - importe_descuento
		importe_iva = base_tras_descuento * IVA		
		total_factura = base_tras_descuento + importe_iva	
		
		############### Información del programa ###############
		print('Impresora de tickets')
		print('Daniel Oliveira Vidal')
		print('2025 - v1.0 (c)')
		print('')
		print('---------------------------------')
		print('')
		
		############### Información cliente ###############
		print('Nombre:', cliente_nombre)
		print('Edad:',edad)
		print('')
		print('---------------------------------')
		print('')
		
		############### Desglose ticket ###############
		print('- Base imponible:', base_imponible)
		print('- Descuento hecho:', descuento_hecho, '%')
		print('- Importe descuento:', importe_descuento)
		print('- Base tras descuento:', base_tras_descuento)
		print('- IVA:', importe_iva)
		print('')
		print('TOTAL:', total_factura)
		print('')
		print('---------------------------------')
		print('')
