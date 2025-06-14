class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad

    def mostrar_datos(self):
        print("Nombre:",self.__nombre)
        print("Edad:",self.__edad)

    def mostrar_nombre(self):
        return self.__nombre


    def modif_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre

class Estudiante(Persona)
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad) # heredp del padre
        self.carrera=carrera

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Carrera: ",self.carrera)
class Profesor(Persona)
    def __init__(self,nombre,edad,asignatura):
        super().__init__(nombre,edad) # heredp del padre
        self.asignatura=asignatura

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Asigna: ",self.asignatura)


persona1= Profesor(**************)
persona2= Estudiante(*********)

