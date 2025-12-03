'''
    Duelo de magos
    v1.0 Daniel Oliveira Vidal
    Este programa pide la edad del mago, lo clasifica en un clase y mediante hechizos tiene que destruir un escudo.
'''

################ Estadísticas magos ################

edad_mago = input('Introduce la edad del mago: ')
try:
    edad_mago = int(edad_mago)
    
except:
    edad_mago = 100
clasificacion_mago = ''
poder_base = 0
    
################ Clasificación ################

if edad_mago < 31:
    clasificacion_mago = 'Aprendiz'
    
elif edad_mago >= 30 and edad_mago < 100:
    clasificacion_mago = 'Hechicero'
    
else:
    clasificacion_mago = 'Archimago'

print('El mago es un', clasificacion_mago)
################ Poderes ################

def poderBase(edad_mago):
    '''
        poderBase
        Entradas: edad_mago
        Salidas: poder_base        
    '''
    if edad_mago < 31:
        poder_base = 5
    
    elif edad_mago >= 30 and edad_mago < 100:
        poder_base = 8
    
    else:
        poder_base = 10
        
    return poder_base

poder_base = poderBase(edad_mago)
print('El mago', clasificacion_mago, 'tiene un poder base de', poder_base)
   
################ Rompimiento del hechizo ################
escudo_magico = 15

for i in range(1, 3):
    print('Turno', i)
    
    if i == 1:
        print('El mago a usado hechizo de fuego')
        daño = poder_base // 2
        
    else:
        print('El mago a usado hechizo de rayo')
        daño = poder_base // 2
    
    
    
    

