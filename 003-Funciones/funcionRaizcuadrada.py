def raizCuadrada (radicando):
    '''
        Función de raíz cuadrada
        Entradas: radicando que se espera que sea numérico
        Salidas: resultado de la raíz cuadrada como número (o cero si es fallo)
        Capturas de error:
         1.-Si es numérico
         2.-Si se puedo convertir a numérico
         3.-Si el número es negativo
    '''
    # Importamos de la librería "math" la función "sqrt" para poder calcular raices
    from math import sqrt
    # Comprobamos si es un número
    print('Entramos en la función')
    if isinstance(radicando, (int, float, complex)):
        print('Parece que el parámetro es un número')
        if radicando >= 0:
            print('Parece que el se puede hacer la raíz de número')
            resultado = sqrt(radicando)
            return resultado
        else:
            print('No puedo hacer la raíz del número por que es negativo')
            resultado = 0
    else:
        print('El parámetro no es un número, voy a intentar convertirlo') 
        try:
            print('Convierto a números con éxito')
            #Vamos a intentar convertirlo a un número
            radicando = float(radicando)
            resultado = sqrt(radicando)
            return resultado
        except:
            print('He intentado convertir a números, pero no he podido')
            return 0
            
            
