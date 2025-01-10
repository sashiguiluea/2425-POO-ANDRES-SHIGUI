# Programa: Calculadora de área y perímetro de un rectángulo
# Este programa solicita al usuario las dimensiones de un rectángulo (base y altura),
# calcula el área y el perímetro, y muestra los resultados al usuario utilizando clases.

class Rectangulo:
    """
    Clase que representa un rectángulo y permite calcular su área y perímetro.
    """
    def __init__(self, base: float, altura: float):
        """
        Inicializa un rectángulo con su base y altura.
        :param base: Base del rectángulo.
        :param altura: Altura del rectángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Calcula el área del rectángulo.
        :return: Área del rectángulo.
        """
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del rectángulo.
        :return: Perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def es_cuadrado(self) -> bool:
        """
        Verifica si el rectángulo es un cuadrado.
        :return: True si es un cuadrado, False en caso contrario.
        """
        return self.base == self.altura

# Solicitar datos al usuario
print("Calculadora de área y perímetro de un rectángulo")

# Variables descriptivas
base_rectangulo: float = float(input("Introduce la base del rectángulo (en metros): "))
altura_rectangulo: float = float(input("Introduce la altura del rectángulo (en metros): "))

# Crear instancia de Rectangulo
rectangulo = Rectangulo(base_rectangulo, altura_rectangulo)

# Cálculos
area: float = rectangulo.calcular_area()
perimetro: float = rectangulo.calcular_perimetro()

# Mostrar resultados
print("\nResultados:")
print(f"Área: {area} metros cuadradas")
print(f"Perímetro: {perimetro} metros")

# Confirmar si las dimensiones son cuadradas
if rectangulo.es_cuadrado():
    print("El rectángulo es, de hecho, un cuadrado.")
