import json

class Producto:
    """
    Esta clase representa un producto individual con atributos como ID, nombre, cantidad y precio.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor de la clase Producto
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto

    def __str__(self):
        # Representación en cadena del producto
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    """
    Esta clase gestiona un inventario de productos, proporcionando métodos para
    agregar, eliminar, actualizar, buscar y mostrar productos.
    """
    def __init__(self):
        # Constructor de la clase Inventario
        self.productos = {}  # Diccionario para almacenar los productos

    def cargar_inventario(self, archivo='inventario.json'):
        """Carga los datos del inventario desde un archivo JSON."""
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)  # Cargar datos desde el archivo JSON
                self.productos = {id_prod: Producto(**info) for id_prod, info in data.items()}  # Convertir datos a objetos Producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            self.productos = {}  # Inicializar inventario vacío
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.productos = {}  # Inicializar inventario vacío en caso de error de formato
        except PermissionError:
            print("Error: No tienes permiso para acceder al archivo de inventario.")

    def guardar_inventario(self, archivo='inventario.json'):
        """Guarda el inventario en un archivo JSON."""
        try:
            with open(archivo, 'w') as f:
                json.dump({id_prod: vars(prod) for id_prod, prod in self.productos.items()}, f, indent=4)  # Guardar productos en JSON
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        if producto.id_producto in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto  # Agregar producto al diccionario
            print(f"Producto {producto.id_producto} agregado.")
            self.guardar_inventario()  # Guardar cambios inmediatamente

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario si existe."""
        if id_producto in self.productos:
            del self.productos[id_producto]  # Eliminar producto del diccionario
            print(f"Producto {id_producto} eliminado.")
            self.guardar_inventario()  # Guardar cambios inmediatamente
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto en el inventario."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad  # Actualizar cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio  # Actualizar precio
            print(f"Producto {id_producto} actualizado.")
            self.guardar_inventario()  # Guardar cambios inmediatamente
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre_producto):
        """Busca productos en el inventario por su nombre."""
        encontrados = [prod for prod in self.productos.values() if nombre_producto.lower() in prod.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)  # Mostrar productos encontrados
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)  # Imprimir cada producto en el inventario

def pedir_entero(mensaje):
    """Solicita un número entero al usuario y maneja errores en la entrada."""
    while True:
        try:
            return int(input(mensaje))  # Solicitar y convertir entrada a entero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def pedir_flotante(mensaje):
    """Solicita un número flotante al usuario y maneja errores en la entrada."""
    while True:
        try:
            return float(input(mensaje))  # Solicitar y convertir entrada a flotante
        except ValueError:
            print("Por favor, ingrese un precio válido.")

def menu():
    inventario = Inventario()  # Crear instancia de Inventario
    inventario.cargar_inventario()  # Cargar inventario desde archivo JSON

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Opción para agregar un producto
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_flotante("Precio: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Opción para eliminar un producto
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Opción para actualizar un producto
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Opción para buscar un producto
            nombre_producto = input("Nombre del Producto a buscar: ")
            inventario.buscar_producto(nombre_producto)
        elif opcion == '5':
            # Opción para mostrar el inventario
            inventario.mostrar_inventario()
        elif opcion == '6':
            # Opción para guardar y salir
            inventario.guardar_inventario()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()  # Iniciar el menú principal

