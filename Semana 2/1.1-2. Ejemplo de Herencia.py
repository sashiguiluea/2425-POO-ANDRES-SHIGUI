class Vehiculo:
    # Constructor de la clase base Vehiculo
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo para almacenar la marca del vehículo
        self.modelo = modelo  # Atributo para almacenar el modelo del vehículo

    # Método para mostrar la identificación básica del vehículo
    def mostrar_identificacion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"  # Devuelve una descripción del vehículo

# Clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    # Constructor de la clase Coche
    def __init__(self, marca, modelo, numeroDePuertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase base Vehiculo
        self.numeroDePuertas = numeroDePuertas  # Atributo adicional específico para Coche

    # Método para mostrar los detalles específicos del coche
    def mostrar_detalles(self):
        informacion_base = super().mostrar_identificacion()  # Obtiene la información de la clase base
        return f"{informacion_base}, con {self.numeroDePuertas} puertas"  # Agrega detalles específicos del coche

# Creando un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla")  # Se inicializa con marca y modelo
print(mi_vehiculo.mostrar_identificacion())  # Imprime la identificación del vehículo

# Creando un objeto de la clase Coche
mi_coche = Coche("Honda", "Civic", 4)  # Se inicializa con marca, modelo y número de puertas
print(mi_coche.mostrar_detalles())  # Imprime los detalles específicos del coche
