class Persona():
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
	def dameDatos(self):
		return self.nombre + self.apellidos

class Profesor(Persona):
	def __init__(self,nombre,apellidos:
		super().__init__(nombre, apellidos)
	def dameDatos(self):
		return 'Profesor: ' + self.nombre + self.apellidos

class Alumno(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre, apellidos)
	def dameDatos(self):
		return 'Alumnos: ' + self.nombre + self.apellidos
    
alumno1 = Alumno('Daniel', 'Oliveira Vidal', 'info@elorange12.com', 'La casa de Daniel')
print(alumno1.dameDatos())

profesor1 = Profesor('Pedro', 'Garcia', 'pedro@elorange12.com', 'La casa de Pedro')
print(profesor1.dameDatos())
