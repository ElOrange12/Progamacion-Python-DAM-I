'''
    Juegos y Valoración
    (c) 2025 Daniel Oliveira Vidal
    Este programa pide un videojuego una puntuación de ese juego y muestra por pantalla el nombre del juego y el doble de su puntuación 
'''
juego = input('Cuál es tu videojuego favorito: ')
valoracion = input('Qué puntuación le das al juego: ')

entero = int(valoracion)

print('Tu videojuego favorito es', juego, 'y el doble de la puntuación es', entero*2)
