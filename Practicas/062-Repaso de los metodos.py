class Gato():
	def __init__ (self):
		self.color = ''		# Esto es una propiedad
		
	def maulla (self):
		return 'miau'		# Esto es un metodo
		
gato1 = Gato()
gato1.color = 'naranja'		# Aquí seteamos una propiedad directamente (No es una buena práctica)
print(gato1.maulla())
