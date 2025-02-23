import os
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
        """Carga el inventario desde un archivo de texto."""

        # Si el archivo no existe, lo crea vacío
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Creando uno nuevo...")
            open(self.archivo, 'w').close()
            return  # No hay nada más que cargar, así que salimos del método

        try:
            # Abre el archivo en modo lectura con Context Managers (with)
            with open(self.archivo, 'r') as f:
                for line in f:
                    producto = Producto.from_string(line)
                    if producto:  # Verificar que la conversión fue exitosa
                        self.productos[producto.id_producto] = producto
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el inventario: {e}")

    # Método para guardar el inventario en el archivo
    def guardar_inventario(self,mensaje=True):
        try:
            # Abre el archivo en modo escritura
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    # Escribe cada producto en el archivo
                    f.write(str(producto) + '\n')
            if mensaje:
                print("Inventario guardado con éxito.")
        except Exception as e:
            # Captura cualquier excepción y muestra un mensaje de error
            print(f"Error al guardar el inventario: {e}")

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Producto ya existe.")  # Informa si el producto ya está en el inventario
        else:
            self.productos[producto.id_producto] = producto  # Agrega el producto al diccionario
            self.guardar_inventario()  # Guarda el inventario en el archivo

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]  # Elimina el producto del diccionario
            self.guardar_inventario()  # Guarda el inventario en el archivo
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
            self.guardar_inventario()  # Guarda el inventario en el archivo
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
            try:
                id_producto = input("ID del Producto: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                if cantidad < 0 or precio < 0:
                    raise ValueError("Cantidad y precio deben ser positivos.")
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Entrada inválida. Asegúrese de ingresar valores correctos.")
        elif opcion == '2':
            # Opción para eliminar un producto
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)  # Elimina el producto del inventario
        elif opcion == '3':
            # Opción para actualizar un producto
            id_producto = input("ID del Producto a actualizar: ").strip()
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ").strip()
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ").strip()
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Entrada inválida para cantidad o precio.")
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