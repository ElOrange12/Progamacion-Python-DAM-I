class Gato():
	def __init__ (self):
		self.color = 'naranja'		# Esto es una propiedad privada (Contrapuesta a pública)
		
		
gato1 = Gato()

print(gato1.__color)
