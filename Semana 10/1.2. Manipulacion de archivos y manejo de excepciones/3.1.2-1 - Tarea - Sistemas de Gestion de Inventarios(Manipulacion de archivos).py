"""
Clase que representa un producto en el inventario.

Atributos:
    id_producto (str): Identificador único del producto.
    nombre (str): Nombre del producto.
    cantidad (int): Cantidad disponible del producto en el inventario.
    precio (float): Precio del producto.
"""
class Producto:
    # Constructor de la clase Producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = precio  # Precio del producto

    # Método para representar el objeto Producto como una cadena
    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    # Método estático para crear un objeto Producto a partir de una línea de texto
    @staticmethod
    def from_string(line):
        try:
            # Separa la línea en componentes y convierte cantidad y precio a sus tipos correspondientes
            id_producto, nombre, cantidad, precio = line.strip().split(',')
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            # Si hay un error en la conversión, devuelve None
            return None

"""
Clase que representa un inventario de productos.

Atributos:
    archivo (str): Nombre del archivo donde se guarda el inventario.
    productos (dict): Diccionario que almacena los productos, usando el ID del producto como clave.
"""
class Inventario:
    # Constructor de la clase Inventario
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo  # Nombre del archivo donde se guarda el inventario
        self.productos = {}  # Diccionario para almacenar los productos
        self.cargar_inventario()  # Carga el inventario desde el archivo

    # Método para cargar el inventario desde el archivo
    def cargar_inventario(self):
        try:
            # Abre el archivo en modo lectura
            with open(self.archivo, 'r') as f:
                for line in f:
                    # Crea un objeto Producto a partir de cada línea y lo agrega al diccionario
                    producto = Producto.from_string(line)
                    if producto:
                        self.productos[producto.id_producto] = producto
        except FileNotFoundError:
            # Si el archivo no se encuentra, informa al usuario
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")

    # Método para guardar el inventario en el archivo
    def guardar_inventario(self):
        try:
            # Abre el archivo en modo escritura
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    # Escribe cada producto en el archivo
                    f.write(str(producto) + '\n')
        except Exception as e:
            # Captura cualquier excepción y muestra un mensaje de error
            print(f"Error al guardar el inventario: {e}")

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Producto ya existe.")  # Informa si el producto ya está en el inventario
        else:
            self.productos[producto.id_producto] = producto  # Agrega el producto al diccionario

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]  # Elimina el producto del diccionario
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")  # Informa si el producto no está en el inventario

    # Método para actualizar la cantidad y/o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad  # Actualiza la cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio  # Actualiza el precio
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")  # Informa si el producto no está en el inventario

    # Método para buscar un producto por su nombre en el inventario.
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre en el inventario.

        Informa al usuario si el producto no se encuentra.
        """
        encontrado = False
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():  # Comparación sin distinguir mayúsculas
                print(
                    f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: ${producto.precio:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado en el inventario.")  # Mensaje si no se encuentra el producto

    # Método para mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")  # Informa si no hay productos
        else:
            for producto in self.productos.values():
                # Muestra cada producto
                print(
                    f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: ${producto.precio:.2f}")

# Función principal que muestra el menú y gestiona las opciones del usuario
def menu():
    inventario = Inventario()  # Crea una instancia de Inventario

    while True:
        # Muestra las opciones del menú
        print(
            "\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción

        if opcion == '1':
            # Opción para agregar un producto
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)  # Crea un nuevo producto
            inventario.agregar_producto(producto)  # Agrega el producto al inventario
            inventario.guardar_inventario()  # Guarda el inventario en el archivo
            print("Inventario guardado con exito...")  # Mensaje de salida
        elif opcion == '2':
            # Opción para eliminar un producto
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)  # Elimina el producto del inventario
            inventario.guardar_inventario()  # Guarda el inventario en el archivo
            print("Inventario eliminado con exito...")  # Mensaje de salida
        elif opcion == '3':
            # Opción para actualizar un producto
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None  # Convierte a int o None
            precio = float(precio) if precio else None  # Convierte a float o None
            inventario.actualizar_producto(id_producto, cantidad, precio)  # Actualiza el producto
            inventario.guardar_inventario()  # Guarda el inventario en el archivo
            print("Inventario actualizadocon exito...")  # Mensaje de salida
        elif opcion == '4':
            # Opción para buscar un producto
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre_producto)  # Busca el producto por nombre
        elif opcion == '5':
            # Opción para mostrar el inventario
            inventario.mostrar_inventario()  # Muestra todos los productos
        elif opcion == '6':
            # Opción para guardar y salir
            inventario.guardar_inventario()  # Guarda el inventario en el archivo
            print("Inventario guardando y Saliendo...")  # Mensaje de salida
            break  # Sale del bucle

# ```python
if __name__ == "__main__":
    menu()  # Llama a la función menu para iniciar el programa