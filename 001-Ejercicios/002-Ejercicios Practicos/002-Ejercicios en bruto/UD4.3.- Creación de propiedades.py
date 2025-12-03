'''
    Clase clientes
    v1.0 Daniel Oliveira Vidal
    Este programa crea una clase clientes con propiedades que tienen arrays
'''
class Cliente():
    def __init__(self):
        self.nombre = ''
        self.edad = 0
        self.telefonos = []

cliente1 = Cliente()
cliente1.nombre = 'Pedro'
cliente1.edad = 28
cliente1.telefonos.append('123456789')
cliente1.telefonos.append('987654321')

print('Nombre:', cliente1.nombre)
print('Edad:', cliente1.edad)
print('Telefonos:', cliente1.telefonos)