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


