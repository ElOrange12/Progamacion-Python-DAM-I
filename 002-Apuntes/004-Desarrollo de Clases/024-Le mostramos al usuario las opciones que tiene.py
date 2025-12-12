'''
    Aplicación de gestión de productos
    (c) 2025 Daniel Oliveira Vidal
    Esta aplicación gestiona productor
'''

# En esta aplicación no aplica librerías

# Definimos clases y funciones

class Producto():
    def __init__ (self):
        self.nombre = ''
        self.precio = 0
        
# Creamos las variables globales

productor = []

# Primero lanzamos un mensaje de bienvenida
print('Gestor de productor v0.1 Daniel Oliveira Vidal')
# Le mostramos al usuario las opciones que tiene 
print('Selecciona una opción: ')
print('1.-Crear un nuevo producto')
print('2.-Listar productos')
print('3.-Actualizar productos')
print('4.-Eliminar productos')
opcion = int(input('Escoge una opción: '))
# En función de la opción que coja el usuario
    # O bien creamos un nuevo producto
    # O bien listamos los productos
    # O bien actualizamos los productos
    # O bien eliminamos los productos
# Y volvemos a repetir
