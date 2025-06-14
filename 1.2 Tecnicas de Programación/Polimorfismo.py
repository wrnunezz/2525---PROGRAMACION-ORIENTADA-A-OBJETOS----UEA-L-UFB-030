# Clase animal
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def sonido(self):
        return "Hace el sonido "


class Perro(Animal):
    def sonido(self):
        return f"{self.nombre} dice : Gua gua"

class Gato(Animal):
    def sonido(self):
        return f"{self.nombre} dice : Miau miu "

# CREAR OBJETOS
animal1 = Perro("Firulais")
animal2 = Gato("Misifu")

# llamr
print(animal1.sonido())