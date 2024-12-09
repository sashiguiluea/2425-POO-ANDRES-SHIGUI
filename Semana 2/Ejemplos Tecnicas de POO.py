# Ejemplo de Conceptos de Programación Orientada a Objetos en Python

from abc import ABC, abstractmethod


# Abstracción: Clase abstracta que define una interfaz común para diferentes tipos de dispositivos
class DispositivoElectronico(ABC):
    """
    Clase abstracta base que representa un dispositivo electrónico.
    Demuestra el concepto de ABSTRACCIÓN al definir una interfaz común
    que las subclases deben implementar.
    """

    def __init__(self, marca: str, modelo: str):
        """
        Constructor que inicializa los atributos básicos de un dispositivo.

        :param marca: Marca del dispositivo
        :param modelo: Modelo del dispositivo
        """
        # Encapsulación: Atributos privados para proteger los datos internos
        self._marca = marca  # Atributo protegido
        self._modelo = modelo
        self._encendido = False  # Estado inicial del dispositivo

    # Método abstracto que obliga a las subclases a implementar el método de encendido
    @abstractmethod
    def encender(self):
        """
        Método abstracto para encender el dispositivo.
        Las subclases DEBEN implementar este método.
        """
        pass

    @abstractmethod
    def apagar(self):
        """
        Método abstracto para apagar el dispositivo.
        Las subclases DEBEN implementar este método.
        """
        pass

    # Método concreto que puede ser usado por todas las subclases
    def obtener_informacion(self):
        """
        Método que proporciona información básica del dispositivo.
        Demuestra cómo los métodos pueden tener implementación en la clase base.

        :return: Cadena con información del dispositivo
        """
        return f"Marca: {self._marca}, Modelo: {self._modelo}"


# Herencia: Subclases que heredan de la clase abstracta base
class Smartphone(DispositivoElectronico):
    """
    Clase Smartphone que hereda de DispositivoElectronico.
    Demuestra el concepto de HERENCIA al extender la clase base.
    """

    def __init__(self, marca: str, modelo: str, sistema_operativo: str):
        """
        Constructor que inicializa un smartphone con atributos adicionales.

        :param marca: Marca del smartphone
        :param modelo: Modelo del smartphone
        :param sistema_operativo: Sistema operativo del smartphone
        """
        # Llamada al constructor de la clase padre
        super().__init__(marca, modelo)
        # Atributo específico de Smartphone
        self._sistema_operativo = sistema_operativo

    # Implementación del método encender (Polimorfismo)
    def encender(self):
        """
        Implementación específica del método encender para Smartphone.
        Demuestra POLIMORFISMO al proporcionar una implementación única.
        """
        if not self._encendido:
            self._encendido = True
            return f"Smartphone {self._marca} {self._modelo} encendido. Sistema operativo: {self._sistema_operativo}"
        return "El smartphone ya está encendido"

    # Implementación del método apagar (Polimorfismo)
    def apagar(self):
        """
        Implementación específica del método apagar para Smartphone.
        Otro ejemplo de POLIMORFISMO.
        """
        if self._encendido:
            self._encendido = False
            return f"Smartphone {self._marca} {self._modelo} apagado"
        return "El smartphone ya está apagado"

    # Método adicional específico de Smartphone
    def tomar_foto(self):
        """
        Método específico de Smartphone.
        Demuestra cómo las subclases pueden añadir funcionalidades propias.
        """
        if self._encendido:
            return "Fotografía capturada"
        return "No se puede tomar foto. El smartphone está apagado"


# Otra subclase para demostrar polimorfismo
class Laptop(DispositivoElectronico):
    """
    Clase Laptop que también hereda de DispositivoElectronico.
    Otro ejemplo de HERENCIA y POLIMORFISMO.
    """

    def __init__(self, marca: str, modelo: str, ram: int):
        """
        Constructor de Laptop con atributo adicional.

        :param marca: Marca de la laptop
        :param modelo: Modelo de la laptop
        :param ram: Memoria RAM de la laptop
        """
        super().__init__(marca, modelo)
        self._ram = ram

    # Implementación polimorfica de encender
    def encender(self):
        """
        Implementación única de encender para Laptop.
        """
        if not self._encendido:
            self._encendido = True
            return f"Laptop {self._marca} {self._modelo} iniciando. RAM: {self._ram}GB"
        return "La laptop ya está encendida"

    # Implementación polimorfica de apagar
    def apagar(self):
        """
        Implementación única de apagar para Laptop.
        """
        if self._encendido:
            self._encendido = False
            return f"Laptop {self._marca} {self._modelo} apagándose"
        return "La laptop ya está apagada"


# Función para demostrar polimorfismo
def probar_dispositivo(dispositivo: DispositivoElectronico):
    """
    Función que demuestra POLIMORFISMO al trabajar con diferentes tipos de dispositivos.

    :param dispositivo: Cualquier dispositivo que herede de DispositivoElectronico
    """
    print(dispositivo.obtener_informacion())
    print(dispositivo.encender())

    # Ejemplo adicional de polimorfismo con método específico
    if isinstance(dispositivo, Smartphone):
        print(dispositivo.tomar_foto())


# Demostración de los conceptos
def main():
    """
    Función principal para mostrar el uso de los conceptos de POO.
    """
    # Crear instancias de diferentes dispositivos
    iphone = Smartphone("Apple", "iPhone 13", "iOS")
    dell = Laptop("Dell", "XPS", 16)

    # Probar polimorfismo
    print("--- Probando Smartphone ---")
    probar_dispositivo(iphone)

    print("\n--- Probando Laptop ---")
    probar_dispositivo(dell)


# Punto de entrada del programa
if __name__ == "__main__":
    main()