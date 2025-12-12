class Persona():
	def __init__(self, nombre, apellidos, email, direccion):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.direccion = direccion
	def dameDatos(self):
		return self.nombre + self.apellidos

class Profesor(Persona):
	def __init__(self,nombre,apellidos,email, direccion):
		super().__init__(nombre, apellidos, email, direccion)

class Alumno(Persona):
	def __init__(self,nombre,apellidos,email, direccion):
		super().__init__(nombre, apellidos, email, direccion)		
    
alumno1 = Alumno('Daniel', 'Oliveira Vidal', 'info@elorange12.com', 'La casa de Daniel')
print(alumno1.dameDatos())

profesor1 = Profesor('Pedro', 'Garcia', 'pedro@elorange12.com', 'La casa de Pedro')
print(profesor1.dameDatos())
