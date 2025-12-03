'''
    Clase cliente
    v1.0 Daniel Oliveira Vidal
    Este programa crea y instacia un clase con metodos setters y getters.
'''

class Cliente():
    def __init__(self):
        self.nombrecompleto = ''
        self.email = ''

    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre

    def getNombreCompleto(self):
        return self.nombrecompleto
    
    def setEmail(self, nuevoemail):
        self.email = nuevoemail

    def getEmail(self):
        return self.email
    
cliente1 = Cliente()
cliente1.nombrecompleto = 'Perico'
cliente1.email = 'info@perico.com'

cliente1.setNombreCompleto('Pepe')
cliente1.getNombreCompleto()

cliente1.setEmail('info@pepe.com')
cliente1.getEmail()
    
