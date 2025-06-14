# ejemplo poo
class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_datos(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)



# #crear objetos
# perro= Animal("Firu",5)
# gato= Animal("Misifu",2)
#
# #llamar
# perro.mostrar_datos()
# gato.mostrar_datos()
