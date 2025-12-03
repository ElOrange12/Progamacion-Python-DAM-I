'''
    Clase Futbolista
    v1.0 Daniel Oliveira Vidal
    Este programa crea una clase y en base a una de sus propiedades hace diferentes metodos
'''

class Futbolista():
    def __init__(self):
        self.nombre = ''
        self.edad = 0 
        self.posicion = ''
    
    def jubilación(self):
        anyos_para_jubilacion = 65 - self.edad
        print('Le quedan', anyos_para_jubilacion, 'para jubilarse')

    def mayor_edad(self):
        if self.edad >= 18:
            print('Es mayor de edad.')

        else:
            print('No es mayor de edad.')

jugador1 = Futbolista()
jugador1.nombre = 'Messi'
jugador1.edad = 38
jugador1.posicion = 'Extremo derecho'

print(jugador1.jubilación())

jugador1.mayor_edad()