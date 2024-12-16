class CuentaBancaria:
    # Constructor de la clase que inicializa el saldo como un atributo privado
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado para proteger el saldo de accesos directos

    # Método para depositar dinero en la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:  # Verifica que la cantidad a depositar sea positiva
            self.__saldo += cantidad  # Incrementa el saldo privado
            print(f"Depositado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")  # Mensaje de error para cantidades negativas

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:  # Verifica que haya suficiente saldo para el retiro
            self.__saldo -= cantidad  # Decrementa el saldo privado
            print(f"Retirado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")  # Mensaje de error si no hay suficiente saldo

    # Método 'getter' para obtener el saldo actual de la cuenta
    def obtener_saldo(self):
        return self.__saldo  # Devuelve el valor del saldo privado

# Creando un objeto de la clase CuentaBancaria
mi_cuenta = CuentaBancaria(1000)  # Se inicializa con un saldo de 1000

# Utilizando los métodos de la clase
print(f"Saldo inicial: {mi_cuenta.obtener_saldo()}")  # Imprime el saldo inicial
mi_cuenta.depositar(500)  # Deposita 500 en la cuenta
mi_cuenta.retirar(200)  # Retira 200 de la cuenta
print(f"Saldo final: {mi_cuenta.obtener_saldo()}")  # Imprime el saldo final
