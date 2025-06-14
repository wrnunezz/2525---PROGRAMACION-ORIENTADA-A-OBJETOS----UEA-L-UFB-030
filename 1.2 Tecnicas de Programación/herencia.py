# herencia
# clase base
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def sonido(self):
        return "Hacer sonido"



class Dog(Animal): # clase hija 1
    def __init__(self,nombre,raza):
        super().__init__(raza)
        self.raza=raza

    def sonido(self):
        return f"{self.nombre} dice: Gua gua "
class Gato(Animal): # clase hija 2
    def __init__(self,nombre,color):
        super().__init__(color)
        self.color=color

    def sonido(self):
        return f"{self.nombre} dice: Miauuuu "
# crear los objetos
dog= Dog("Firulais","Chiguagua")
cat = Gato("Misifu","Negro")

#print(dog.nombre)

print(dog.sonido())
print(cat.sonido())