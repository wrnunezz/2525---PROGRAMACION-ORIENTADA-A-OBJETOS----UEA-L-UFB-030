# vehiculos
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca:{self.marca}, modelo:{self.modelo}"
class Auto(Vehiculo): # clase Hija
    def __init__(self,marca,modelo,puertas):
        super().__init__(marca,modelo) # llamo al const
        self.puertas = puertas

    def descripcion(self):
        return f"{super().descripcion()}, puertas:{self.puertas}"
class Camion(Vehiculo): #calse hija
    def __init__(self,marca,modelo,capacidad):
        super().__init__(marca,modelo)
        self.capacidad = capacidad

    def descripcion(self):
        return f"{super().descripcion()}, capacidad:{self.capacidad}"

auto= Auto("Nissan","Versa ","5")
camion1 = Camion("HINO","AK","20")

print(auto.descripcion())
print(camion1.descripcion())
