import os  # Importa el módulo 'os' para interactuar con el sistema operativo.

# Función para mostrar el código fuente de un archivo dado.
def mostrar_codigo(ruta_script):
    # Convierte la ruta relativa en una ruta absoluta.
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Intenta abrir el archivo en modo lectura ('r').
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")  # Muestra el nombre del archivo.
            print(archivo.read())  # Lee y muestra el contenido del archivo.
    except FileNotFoundError:
        # Maneja el error si el archivo no se encuentra.
        print(f"El archivo '{ruta_script}' no se encontró. Verifica que la ruta sea correcta.")
    except Exception as e:
        # Maneja cualquier otro tipo de error.
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función que muestra el menú y permite seleccionar un script para ver su código.
def mostrar_menu():
    # Obtiene la ruta del directorio donde se encuentra el script actual.
    ruta_base = os.path.dirname(__file__)

    # Diccionario con las opciones del menú y sus rutas de archivos correspondientes.
    opciones = {
        '1': 'Semana 2/1.1-1. Ejemplo de Abstracción.py',
        '2': 'Semana 2/1.1-2. Ejemplo de Herencia.py',
        '3': 'Semana 2/1.1-3. Ejemplo de Encapsulacion.py',
        '4': 'Semana 2/1.1-4. Ejemplo de Polimorfismo.py',
        '5': 'Semana 2/Ejemplos Tecnicas de POO.py',
        '6': 'Semana 3/2.1-1. Tarea Programación Tradicional.py',
        '7': 'Semana 3/2.1-2. Tarea Programacion Orientada a Objetos.py',
        '8': 'Semana 4/2.2-1. Tarea - Relacion Alumno Curso.py',
        '9': 'Semana 4/2.2-2. Tarea - Reserva Hotel.py',
        '10': 'Semana 4/2.2-3. Tarea - Reserva Hotel 2.py',
        '11': 'Semana 4/2.2-4. Tarea - Tienda.py',
        '12': 'Semana 5/2.1.1-1. Tarea - Rectangulo.py',
        '13': 'Semana 6/CuentaBancaria.py',
        '14': 'Semana 7/2.2.1-1 Uso de destructores.py'
        # Se pueden agregar más archivos si es necesario.
    }

    while True:
        print("\n******** Menu Principal - Dashboard ********")
        # Imprime las opciones del menú.
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        # Solicita al usuario que seleccione una opción.
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            # Sale del programa si el usuario elige '0'.
            print("Saliendo del programa.")
            break
        elif eleccion in opciones:
            # Construye la ruta absoluta del script seleccionado.
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            if os.path.exists(ruta_script):  # Verifica si la ruta existe.
                mostrar_codigo(ruta_script)  # Llama a la función para mostrar el código.
            else:
                print(f"El archivo '{ruta_script}' no existe. Verifica la ruta.")
        else:
            # Muestra un mensaje si la opción ingresada no es válida.
            print("Opción no válida. Por favor, intenta de nuevo.")

# Punto de entrada del programa.
if __name__ == "__main__":
    mostrar_menu()  # Llama a la función principal para mostrar el menú.
