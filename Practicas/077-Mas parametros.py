class Gato()
	def __init__(self, edad, nombre): 	# El constructor se ejecuta si o si.
		self.edad = edad
		self.nombre = nombre
		
	def maulla(self):
		return 'El gato está maullando'
		
gato1 = Gato(5, 'micifu')
