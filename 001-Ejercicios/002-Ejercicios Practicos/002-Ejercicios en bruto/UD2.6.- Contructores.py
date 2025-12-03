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

 
