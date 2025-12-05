class Profesor():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email

class Alumno():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
    
alumno1 = Alumno('Daniel', 'Oliveira Vidal', 'info@elorange12.com')
print(alumno1)

profesor1 = Profesor('Pedro', 'Garcia', 'pedro@elorange12.com')
print(profesor1)
