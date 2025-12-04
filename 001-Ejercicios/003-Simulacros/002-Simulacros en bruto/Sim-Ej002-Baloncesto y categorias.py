'''
    Baloncesto y categorías
    v0.1 Daniel Oliveira Vidal
    Este programa te dice en que categoría de baloncesto en la que estas dependiendo de tu edad
'''
# Preguntamos la edad en números enteros
edad = int(input('Dime tu edad: '))

# Utilizamos las estructuras de control if/elif/else para saber en que categoría se encuentra el usuario
if edad < 8:
    categoria = 'pre-mini'
    
elif edad >= 8 and edad < 12:
    categoria = 'mini'
    
elif edad >= 12 and edad < 16:
    categoria = 'infantil'
    
elif edad >= 16 and edad < 18:
    categoria = 'cadete'
    
elif edad >= 18 and edad < 20:
    categoria = 'junior'
    
else:
    categoria = 'senior'

# Mostramos por pantalla la edad del usuario y su categoría
print('Tu edad es de', edad,'entonces estas en la categoría', categoria)

# Además si el jugador sobre pasa los 40 mostramos por pantalla lo siguiente:
if edad > 40:
    print('Además eres un veterano con experiencia en la cancha')
    
