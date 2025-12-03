En este ejercicio se trabaja el concepto de programación orientada a objetos aplicado a la gestión de múltiples datos dentro de una misma clase. 

El objetivo es que el estudiante comprenda que las propiedades de una clase no solo pueden almacenar valores simples, sino también estructuras como listas (arrays).

Esto permite guardar varios elementos relacionados con un mismo objeto, como ocurre en este caso con los números de teléfono de un cliente.

---

Primero de todo declaramos nuestra clase `Cliente`, con su constructor para las propiedades:

```
    class Cliente():
        def __init__(self):
            self.nombre = ''
            self.edad = 0
            self.telefonos = []
```

Ahora instanciamos un objeto, a este lo llamaremos `cliente1`:

```
    cliente1 = Cliente()
    cliente1.nombre = 'Pedro'
    cliente1.edad = 28
    cliente1.telefonos.append('123456789')
    cliente1.telefonos.append('987654321') 
```

Por ultimo lo mostraremos por pantalla:

```
    print('Nombre:', cliente1.nombre)
    print('Edad:', cliente1.edad)
    print('Telefonos:', cliente1.telefonos)
```

---

A continuación se muestra un ejemplo de código del ejemplo resuelto:
 
```
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
```

**Notas:**

- Para poder añadir algo a una lista debemos utilizas la propiedad `.append`.
- Son buenas practicas poner un 0 si es un número o una cadena vacia si es una cadena de texto a las propiedades vacias.

---

Este programa demuestra cómo una clase puede contener propiedades basadas en listas para almacenar múltiples valores asociados a un objeto. 

Gracias a ello, el alumno comprende una técnica fundamental para modelar información más compleja dentro de aplicaciones reales, haciendo el código más flexible y escalable.

Este tipo de estructuras permitirá, en ejercicios futuros, gestionar datos más completos y sistemas más avanzados.