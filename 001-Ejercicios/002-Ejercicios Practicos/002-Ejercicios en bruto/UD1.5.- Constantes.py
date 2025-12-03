'''
    Gravedad y Caida
    v1.0 Daniel Oliveira Vidal
    Este programa calcula cuanto tardaría un objeto en caer al suelo desde una altura de 10.
'''
from math import sqrt

# Estoy usando python no existe la distinción entre constantes y variables, lo pongo en mayúsculas para diferenciarlo
GRAVEDAD = 9.8

altura = 10

# No existe en ninguna función frac en ninguna librería de python, por lo que usaremos "/" para dividir
tiempo_caida = sqrt(2*altura / GRAVEDAD)

print('El objeto caerá en', tiempo_caida)
