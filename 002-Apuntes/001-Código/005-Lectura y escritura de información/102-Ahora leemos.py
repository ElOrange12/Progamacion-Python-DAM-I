archivo = open('clientes.txt', 'r')		# "r" sirve para leer

contenido = archivo.readline()
# También existe archivo.readlines()

print(contenido)

archivo.close()
