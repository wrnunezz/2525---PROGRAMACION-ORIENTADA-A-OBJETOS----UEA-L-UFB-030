# # ejemplo poo
# class Animal:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def mostrar_datos(self):
#         print("Nombre:", self.nombre)
#         print("Edad:", self.edad)
#
#     def hacer_sonido(self):
#         print("Este va hacer el sonido")
#
# class Perro(Animal):
#     def __init__(self,nombre,edad,sonido):
#         super().__init__(nombre,edad) # hereda
#         self.sonido=sonido
#
#     def hacer_sonido(self):
#         print(f"{self.nombre} dice :{self.sonido}")
#
# class Gato(Animal):
#     def __init__(self,nombre,edad,sonido):
#         super().__init__(nombre,edad) # hereda
#         self.sonido=sonido
#
#     def hacer_sonido(self):
#         print(f"{self.nombre} dice :{self.sonido}")
#
# # crear obejtos
# perro= Perro("Firu",5,"GUA GUA")
# gato= Gato("Misifu",2,"Mia miau")
#
# perro.mostrar_datos()
# perro.hacer_sonido()

print("************* polimorfsimo ***********")
# ejemplo poo
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def hacer_sonido(self):
        print("Este va hacer el sonido")

class Perro(Animal):
    def __init__(self,nombre,edad,sonido):
        super().__init__(nombre,edad) # hereda
        self.sonido=sonido

    def hacer_sonido(self):
        print(f"{self.nombre} dice :{self.sonido}")

class Gato(Animal):
    def __init__(self,nombre,edad,sonido):
        super().__init__(nombre,edad) # hereda
        self.sonido=sonido

    def hacer_sonido(self):
        print(f"{self.nombre} dice :{self.sonido}")

