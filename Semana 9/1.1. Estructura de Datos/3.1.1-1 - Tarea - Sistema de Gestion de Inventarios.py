class Producto:
    """
    Clase que representa un producto en el inventario.

    Atributos:
    - id_producto: Identificador único del producto.
    - nombre: Nombre del producto.
    - cantidad: Cantidad disponible del producto en el inventario.
    - precio: Precio del producto.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa un objeto Producto con un ID único, nombre, cantidad y precio.
        self.id_producto = id_producto  # Se asume que el ID del producto es único para evitar confusiones.
        self.nombre = nombre  # El nombre es esencial para la identificación del producto.
        self.cantidad = cantidad  # La cantidad permite gestionar el stock disponible.
        self.precio = precio  # El precio es necesario para las transacciones.

    def __str__(self):
        # Método para representar el objeto Producto como una cadena.
        # Facilita la visualización del producto en el inventario.
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


class Inventario:
    """
    Clase que gestiona un conjunto de productos en el inventario.

    Atributos:
    - productos: Diccionario que almacena los productos, usando el ID del producto como clave.
    """

    def __init__(self):
        # Inicializa un objeto Inventario que contiene un diccionario de productos.
        self.productos = {}  # Se utiliza un diccionario para un acceso rápido a los productos por su ID.

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.

        Si el producto ya existe (mismo ID), se muestra un mensaje de error.
        """
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")  # Evita duplicados en el inventario.
        else:
            self.productos[producto.id_producto] = producto  # Agrega el producto al diccionario.

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.

        Si el producto no se encuentra, se muestra un mensaje de error.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]  # Elimina el producto si existe.
        else:
            print("Error: Producto no encontrado.")  # Manejo de errores si el producto no existe.

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto existente.

        Si el producto no se encuentra, se muestra un mensaje de error.
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad  # Actualiza la cantidad si se proporciona.
            if precio is not None:
                self.productos[id_producto].precio = precio  # Actualiza el precio si se proporciona.
        else:
            print("Error: Producto no encontrado.")  # Manejo de errores si el producto no existe.

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (insensible a mayúsculas/minúsculas).

        Imprime los productos que coinciden con el nombre buscado.
        """
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():  # Compara nombres sin importar mayúsculas/minúsculas.
                print(producto)  # Imprime el producto si se encuentra.

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.

        Imprime cada producto en el inventario, facilitando la gestión visual del stock.
        """
        for producto in self.productos.values():
            print(producto)  # Imprime cada producto en el inventario.


def menu():
    """
    Función principal que maneja la interacción con el usuario.

    Permite al usuario agregar, eliminar, actualizar, buscar y mostrar productos en el inventario.
    """
    inventario = Inventario()  # Crea una instancia de Inventario.
    while True:
        # Muestra un menú de opciones al usuario.
        print(
            "\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")  # Captura la opción seleccionada por el usuario.
        if opcion == '6':
            break  # Sale del bucle si el usuario elige salir.
        elif opcion == '1':
            # Captura los datos del nuevo producto.
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))  # Convierte la cantidad a entero.
            precio = float(input("Ingrese el precio del producto: "))  # Convierte el precio a float.
            producto = Producto(id_producto, nombre, cantidad, precio)  # Crea un nuevo objeto Producto.
            inventario.agregar_producto(producto)  # Agrega el producto al inventario.
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)  # Elimina el producto del inventario.
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            # Convierte la cantidad y el precio a sus tipos correspondientes si no están vacíos.
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)  # Actualiza el producto.
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)  # Busca el producto por nombre.
        elif opcion == '5':
            inventario.mostrar_inventario()  # Muestra todos los productos en el inventario.


if __name__ == "__main__":
    menu()  # Llama a la función menu para iniciar la aplicación. ```python
