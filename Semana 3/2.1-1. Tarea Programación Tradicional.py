# Programación Tradicional

# Define una función para ingresar temperaturas de los 7 días de la semana
def ingresar_temperaturas():
    # Inicializa una lista vacía para almacenar las temperaturas
    temperaturas = []
    # Itera sobre un rango de números del 1 al 7, representando los días de la semana
    for dia in range(1, 8):
        # Solicita al usuario ingresar la temperatura para el día actual
        # Convierte la entrada a un número decimal con float()
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        # Agrega la temperatura ingresada a la lista de temperaturas
        temperaturas.append(temp)
    # Devuelve la lista completa de temperaturas ingresadas
    return temperaturas

# Define una función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    # Suma todos los elementos de la lista de temperaturas y divide entre la cantidad de elementos
    promedio = sum(temperaturas) / len(temperaturas)
    # Devuelve el promedio calculado
    return promedio

# Entrada de datos
# Llama a la función ingresar_temperaturas() para capturar las temperaturas y las almacena en una variable
temperaturas_tradicional = ingresar_temperaturas()

# Cálculo y salida
# Llama a la función calcular_promedio_semanal() para calcular el promedio de las temperaturas ingresadas
promedio_tradicional = calcular_promedio_semanal(temperaturas_tradicional)
# Imprime el promedio semanal calculado con un mensaje explicativo
print(f"El promedio semanal de temperatura es: {promedio_tradicional}")
