import os  # Importa el módulo os para interactuar con el sistema operativo
import subprocess  # Importa el módulo subprocess para ejecutar comandos del sistema

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)  # Convierte la ruta del script a una ruta absoluta
    try:
        with open(ruta_script_absoluta, 'r') as archivo:  # Intenta abrir el archivo en modo lectura
            codigo = archivo.read()  # Lee el contenido del archivo
            print(f"\n--- Código de {ruta_script} ---\n")  # Imprime un encabezado con el nombre del script
            print(codigo)  # Imprime el código del script
            return codigo  # Devuelve el código leído
    except FileNotFoundError:
        print("El archivo no se encontró.")  # Maneja el caso en que el archivo no existe
        return None  # Devuelve None si no se encuentra el archivo
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")  # Maneja cualquier otro error que ocurra
        return None  # Devuelve None en caso de error

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Verifica si el sistema operativo es Windows
            subprocess.run(['python', ruta_script], check=True)  # Ejecuta el script usando python en Windows
        else:  # Para sistemas basados en Unix
            subprocess.run(['python3', ruta_script], check=True)  # Ejecuta el script usando python3
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")  # Maneja cualquier error que ocurra al ejecutar el script

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)  # Obtiene la ruta del directorio donde se encuentra este archivo

    # Diccionario que mapea números a nombres de semanas
    unidades = {
        '1': 'Semana 2',
        '2': 'Semana 3',
        '3': 'Semana 4',
        '4': 'Semana 5',
        '5': 'Semana 6',
        '6': 'Semana 7'
    }

    while True:  # Bucle infinito para mostrar el menú
        print("\nMenu Principal - Dashboard")  # Imprime el encabezado del menú principal
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")  # Imprime cada opción de unidad
        print("0 - Salir")  # Opción para salir del programa

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")  # Solicita al usuario que elija una unidad
        if eleccion_unidad == '0':  # Si el usuario elige salir
            print("Saliendo del programa.")  # Imprime mensaje de salida
            break  # Sale del bucle
        elif eleccion_unidad in unidades:  # Si la elección es válida
            mostrar_scripts(os.path.join(ruta_base, unidades[eleccion_unidad]))  # Muestra los scripts de la unidad seleccionada
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje de error si la opción no es válida

def mostrar_scripts(ruta_unidad):
    # Obtiene una lista de scripts Python en la ruta de la unidad
    scripts = [f.name for f in os.scandir(ruta_unidad) if f.is_file() and f.name.endswith('.py')]  # Filtra los archivos .py

    while True:  # Bucle infinito para mostrar los scripts
        print("\nScripts - Selecciona un script para ver y ejecutar")  # Imprime el encabezado de scripts
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):  # Enumera los scripts
            print(f"{i} - {script}")  # Imprime cada script con su número correspondiente
        print("0 - Regresar al menú principal")  # Opción para regresar al menú principal

        eleccion_script = input("Elige un script o '0' para regresar: ")  # Solicita al usuario que elija un script
        if eleccion_script == '0':  # Si el usuario elige regresar
            break  # Sale del bucle
        else:
            try:
                eleccion_script = int(eleccion_script) - 1  # Convierte la elección a un índice (restando 1)
                if  0 <= eleccion_script < len(scripts):  # Verifica si la elección está dentro del rango de scripts
                    ruta_script = os.path.join(ruta_unidad, scripts[eleccion_script])  # Construye la ruta del script seleccionado
                    codigo = mostrar_codigo(ruta_script)  # Muestra el código del script
                    if codigo:  # Si se obtuvo código
                        print("Ejecutando el script...\n")  # Imprime mensaje de ejecución
                        ejecutar_codigo(ruta_script)  # Ejecuta el script
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje de error si la opción no es válida
            except ValueError:  # Captura errores de conversión de tipo
                print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje de error si la entrada no es un número

# Ejecutar el dashboard
if __name__ == "__main__":  # Verifica si este archivo es el principal
    mostrar_menu()  # Llama a la función para mostrar el menú ```python