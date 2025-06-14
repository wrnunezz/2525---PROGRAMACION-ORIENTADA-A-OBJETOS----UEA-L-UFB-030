# clase persona
class Persona:
    # constructor
    def __init__(self,nombre, apellido,edad):
        self.nombre=nombre
        self.apellido = apellido
        self.edad = edad

# crear objetos
persona = Persona("Juan","Perez","23")
persona2= Persona("Pedro","Vite","23")

print(persona.nombre)
print(persona.apellido)

print(persona2.nombre)