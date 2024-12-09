# Programación Orientada a Objetos (POO)

# Define una clase que representará el clima de una semana
class ClimaSemana:
    # Método constructor que se ejecuta al crear una instancia de la clase
    def __init__(self):
        # Inicializa un atributo de instancia para almacenar las temperaturas
        self.temperaturas = []

    # Método para ingresar las temperaturas de los 7 días
    def ingresar_temperaturas(self):
        # Itera sobre un rango de números del 1 al 7, representando los días de la semana
        for dia in range(1, 8):
            # Solicita al usuario que ingrese la temperatura del día actual
            # Convierte la entrada a un número decimal con float()
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            # Agrega la temperatura ingresada al atributo `self.temperaturas`
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio_semanal(self):
        # Suma todos los elementos de la lista de temperaturas y divide entre la cantidad de elementos
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        # Devuelve el promedio calculado
        return promedio

# Creación de un objeto de la clase ClimaSemana
# Se crea una instancia de la clase, inicializando el atributo `temperaturas`
clima_poo = ClimaSemana()

# Entrada de datos
# Llama al método `ingresar_temperaturas()` del objeto `clima_poo` para capturar las temperaturas
clima_poo.ingresar_temperaturas()

# Cálculo y salida
# Llama al método `calcular_promedio_semanal()` para calcular el promedio de las temperaturas ingresadas
promedio_poo = clima_poo.calcular_promedio_semanal()
# Imprime el promedio semanal calculado con un mensaje explicativo
print(f"El promedio semanal de temperatura es: {promedio_poo}")
