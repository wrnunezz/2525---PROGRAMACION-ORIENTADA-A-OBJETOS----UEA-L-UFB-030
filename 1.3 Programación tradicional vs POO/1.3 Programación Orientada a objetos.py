# poo
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_datos(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

#crear un objeto

persona1= Persona("Pedro",19)
persona2= Persona("Juan",15)

persona2.mostrar_datos()

