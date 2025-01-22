# Definición de la clase base
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Constructor que inicializa los atributos de la cuenta bancaria."""
        self.titular = titular  # Atributo público
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado)
        print(f"Cuenta bancaria creada para {self.titular} con saldo inicial de {self.__saldo}.")

    def __del__(self):
        """Destructor que notifica la eliminación del objeto de la cuenta bancaria."""
        print(f"La cuenta bancaria de {self.titular} ha sido cerrada y sus recursos liberados.")

    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad} en la cuenta de {self.titular}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        """Método para retirar dinero de la cuenta."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta de {self.titular}.")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    def obtener_saldo(self):
        """Método para acceder al saldo de la cuenta."""
        return self.__saldo

# Definición de la clase derivada
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.02):
        """Constructor que inicializa una cuenta de ahorro con una tasa de interés."""
        super().__init__(titular, saldo_inicial)  # Llamada al constructor de la clase base
        self.tasa_interes = tasa_interes  # Atributo específico de CuentaAhorro

    def aplicar_interes(self):
        """Método para aplicar interés al saldo."""
        interes = self.obtener_saldo() * self.tasa_interes
        self.depositar(interes)  # Usando el método depositar de la clase base
        print(f"Se ha aplicado un interés de {interes} a la cuenta de {self.titular}.")

# Definición de otra clase derivada
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, limite_descubierto=500):
        """Constructor que inicializa una cuenta corriente con un límite de descubierto."""
        super().__init__(titular, saldo_inicial)  # Llamada al constructor de la clase base
        self.limite_descubierto = limite_descubierto  # Atributo específico de CuentaCorriente

    def retirar(self, cantidad):
        """Sobrescribiendo el método retirar para permitir el descubierto."""
        if 0 < cantidad <= (self.obtener_saldo() + self.limite_descubierto):
            self._CuentaBancaria__saldo -= cantidad  # Accediendo al atributo privado de la clase base
            print(f"Se han retirado {cantidad} de la cuenta de {self.titular}.")
        else:
            print("Fondos insuficientes o cantidad no válida.")

# Función para mostrar información de la cuenta
def mostrar_informacion_cuenta(cuenta):
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: {cuenta.obtener_saldo()}")

# Creación de instancias de las clases
cuenta_ahorro = CuentaAhorro("Andrés Shigui", 1000)
cuenta_corriente = CuentaCorriente("Alejandra Noteno", 500)

# Uso de métodos de las clases
cuenta_ahorro.depositar(200)
cuenta_ahorro.retirar(100)
cuenta_ahorro.aplicar_interes()
mostrar_informacion_cuenta(cuenta_ahorro)

cuenta_corriente.depositar(300)
cuenta_corriente.retirar(700)  # Retiro que utiliza el límite de descubierto
mostrar_informacion_cuenta(cuenta_corriente)

# Liberación de recursos manual mediante destructores
del cuenta_ahorro
del cuenta_corriente
