class Cliente():
	def __init__(self, nuevonombre, nuevoemail):
		self.nombre = nuevonombre
		self.email = nuevoemail
		
clientes = []

clientes.append(Cliente('Daniel','info@elorange12.com'))
clientes.append(Cliente('Jose Vicente','info@jocarsa.com'))

print(clientes)
