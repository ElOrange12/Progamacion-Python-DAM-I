class Gato():
	def __init__ (self):
		self.color = ''		# Esto es una propiedad
		
	def maulla (self):
		return 'miau'		# Esto es un metodo
		
	def setColor (self, nuevocolor): 	# Defino un setter - el metodo es el responsable de cambiar la propiedad
		# Por ejemplo aquí podría validar si el color es un color válido para un gato
		self.color = nuevocolor 			# Y cambio la propiedad
	
	def getColor(self):
		# Una vez más, aquí podría poner validaciones si lo quisiera
		return self.color
		
gato1 = Gato()
gato1.color = 'naranja'		# Aquí seteamos una propiedad directamente (No es una buena práctica)

gato1.setColor('naranja')	# Esto es una práctica mucho mejor

print(gato1.color)		# Acceso directo, se puede pero no se recomienda

print(gato1.getColor()) # Acceso mediante método, se recomienda
