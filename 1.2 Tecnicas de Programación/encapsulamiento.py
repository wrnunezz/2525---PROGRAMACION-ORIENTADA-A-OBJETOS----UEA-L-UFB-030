## ejemplo de encapsulamiento

class Cuenta_bancaria:
    def __init__(self,titualar, saldo):
        self.titular=titualar
        self.__saldo=saldo ## privado

    def depositar(self,monto):
        self.__saldo +=monto
    def imprimir_saldo(self):
        return self.__saldo

#cuenta
cuenta= Cuenta_bancaria("Juan",1000)
cuenta.depositar(100)
print(cuenta.imprimir_saldo())