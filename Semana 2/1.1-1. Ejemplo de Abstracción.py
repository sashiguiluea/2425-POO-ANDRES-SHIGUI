from abc import ABC, abstractmethod

# Clase abstracta base que define un esquema común para diferentes tipos de cuentas bancarias
class CuentaBancaria(ABC):
    def __init__(self, titular, saldo_inicial):
        self.titular = titular  # Atributo para almacenar el nombre del titular de la cuenta
        self.saldo = saldo_inicial  # Atributo para almacenar el saldo inicial

    @abstractmethod  # Decorador que indica que este método debe implementarse en las subclases
    def retirar(self, cantidad):
        pass  # Método abstracto sin implementación en la clase base

    @abstractmethod
    def depositar(self, cantidad):
        pass  # Método abstracto sin implementación en la clase base

    # Método común para todas las subclases que muestra el saldo actual
    def mostrar_saldo(self):
        return f"El saldo actual de {self.titular} es: {self.saldo}"  # Devuelve el saldo actual

# Subclase que implementa los métodos abstractos para una cuenta de ahorros
class CuentaAhorros(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad <= self.saldo:  # Verifica si hay suficiente saldo
            self.saldo -= cantidad  # Deduce la cantidad del saldo
            print(f"Se han retirado {cantidad} de la cuenta de ahorros.")
        else:
            print("Fondos insuficientes en la cuenta de ahorros.")

    def depositar(self, cantidad):
        if cantidad > 0:  # Verifica que la cantidad a depositar sea positiva
            self.saldo += cantidad  # Incrementa el saldo
            print(f"Se han depositado {cantidad} en la cuenta de ahorros.")
        else:
            print("La cantidad a depositar debe ser positiva.")

# Subclase que implementa los métodos abstractos para una cuenta corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, limite_credito):
        super().__init__(titular, saldo_inicial)  # Llama al constructor de la clase base
        self.limite_credito = limite_credito  # Atributo adicional para el límite de crédito

    def retirar(self, cantidad):
        if cantidad <= self.saldo + self.limite_credito:  # Verifica si se puede usar el crédito
            self.saldo -= cantidad  # Deduce la cantidad del saldo (o usa crédito si es necesario)
            print(f"Se han retirado {cantidad} de la cuenta corriente.")
        else:
            print("Fondos insuficientes, incluso considerando el crédito disponible.")

    def depositar(self, cantidad):
        if cantidad > 0:  # Verifica que la cantidad a depositar sea positiva
            self.saldo += cantidad  # Incrementa el saldo
            print(f"Se han depositado {cantidad} en la cuenta corriente.")
        else:
            print("La cantidad a depositar debe ser positiva.")

# Creando un objeto de la clase CuentaAhorros
cuenta_ahorros = CuentaAhorros("Juan Perez", 5000)  # Se inicializa con titular y saldo inicial
cuenta_ahorros.depositar(2000)  # Deposita 2000
cuenta_ahorros.retirar(1500)  # Retira 1500
print(cuenta_ahorros.mostrar_saldo())  # Muestra el saldo actual

# Creando un objeto de la clase CuentaCorriente
cuenta_corriente = CuentaCorriente("Ana Lopez", 3000, 1000)  # Se inicializa con titular, saldo inicial y límite de crédito
cuenta_corriente.depositar(1000)  # Deposita 1000
cuenta_corriente.retirar(3500)  # Retira 3500 (incluye uso de crédito)
print(cuenta_corriente.mostrar_saldo())  # Muestra el saldo actual
