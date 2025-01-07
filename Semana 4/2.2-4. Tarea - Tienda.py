# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.stock = stock  # Cantidad disponible en inventario

    def reducir_stock(self, cantidad):
        """Reduce el stock del producto si hay suficiente cantidad."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False

    def __str__(self):
        return f'Producto: {self.nombre} - ${self.precio:.2f} - Stock: {self.stock}'


# Clase que representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Email del cliente

    def __str__(self):
        return f'Cliente: {self.nombre} - Email: {self.email}'


# Clase que representa un pedido en la tienda
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente  # Cliente que realiza el pedido
        self.productos = []  # Lista de productos en el pedido
        self.total = 0.0  # Total del pedido

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al pedido."""
        if producto.reducir_stock(cantidad):
            self.productos.append((producto, cantidad))
            self.total += producto.precio * cantidad
        else:
            print(f'Error: Stock insuficiente para el producto {producto.nombre}.')

    def __str__(self):
        productos_str = "\n".join(
            [f'- {prod.nombre} x{cantidad} - ${prod.precio * cantidad:.2f}' for prod, cantidad in self.productos]
        )
        return f'Pedido de {self.cliente.nombre}:\n{productos_str}\nTotal: ${self.total:.2f}'


# Clase que representa la tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tienda
        self.productos = []  # Lista de productos disponibles
        self.pedidos = []  # Lista de pedidos realizados

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        self.productos.append(producto)

    def listar_productos(self):
        """Muestra los productos disponibles en la tienda."""
        print(f"\nProductos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto)

    def realizar_pedido(self, cliente, productos_pedidos):
        """Realiza un pedido con los productos solicitados por el cliente."""
        pedido = Pedido(cliente)
        for codigo, cantidad in productos_pedidos:
            producto = next((p for p in self.productos if p.codigo == codigo), None)
            if producto:
                pedido.agregar_producto(producto, cantidad)
            else:
                print(f'Error: Producto con código {codigo} no encontrado.')
        self.pedidos.append(pedido)
        print(f'\nPedido realizado con éxito:\n{pedido}')

    def listar_pedidos(self):
        """Muestra todos los pedidos realizados."""
        print(f"\nPedidos realizados en {self.nombre}:")
        for pedido in self.pedidos:
            print(pedido)


# ---- Ejecución ----

# Crear una tienda
tienda = Tienda("Tienda Python")

# Agregar productos al inventario
tienda.agregar_producto(Producto(101, "Laptop", 1000.00, 5))
tienda.agregar_producto(Producto(102, "Mouse", 20.00, 50))
tienda.agregar_producto(Producto(103, "Teclado", 50.00, 20))

# Crear un cliente
cliente = Cliente("Andrés", "andres@example.com")

# Mostrar productos disponibles
tienda.listar_productos()

# Realizar un pedido
productos_pedidos = [(101, 1), (102, 2), (103, 1)]  # Código del producto y cantidad
tienda.realizar_pedido(cliente, productos_pedidos)

# Mostrar productos disponibles después del pedido
tienda.listar_productos()

# Mostrar todos los pedidos realizados
tienda.listar_pedidos()
