'''
	Clase cliente
	v1.0 Daniel Oliveira Vidal
	Este programa almacena mediante una clase, setters y getters cierta información de un cliente
'''
class Cliente():
	def __init__(self, nombre, apellidos, email, edad):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.edad = edad
	
	def setNombre(self, nuevonombre):
		self.nombre = nuevonombre
		
	def setApellidos(self, nuevosapellidos):
		self.apellidos = nuevosapellidos
		
	def setEmail(self, nuevoemail):
		self.email = nuevoemail
		
	def setEdad(self, nuevaedad):
		self.edad = nuevaedad
		
	def getNombre(self):
		return self.email
		
	def getApellidos(self):
		return self.email
			
	def getEmail(self):
		return self.email
		
	def getEdad(self):
		return self.edad
		
cliente1 = Cliente('Pedro', 'Perez Pozo', 'pedro@pepozo.com', 21)
cliente2 = Cliente('Patricia', 'Pardo Pineda', 'patricia@papineda.com', 46)
cliente3 = Cliente('Paco', 'Parker Pinzón', 'paco@papinzon.com', 58)

cliente1.setEdad(23)
print(cliente1.getEdad())

cliente2.setEdad(47)
print(cliente2.getEdad())

cliente2.setEdad(61)
print(cliente2.getEdad())



