'''
    Clasificatoria Edad
    v1.0 Daniel Oliveira Vidal
    Este programa clasifica en niño, adolescente, joven o no joven a jugadores según su edad
'''

edad_jugador = 25

if edad_jugador < 10:
    print('Es un niño')
    
elif edad_jugador >= 10 and edad_jugador < 20:
    print('Es un adolescente')
    
elif edad_jugador >= 20 and edad_jugador < 30:
    print('Es un joven')
    
else:
    print('Ya no eres joven')
    

