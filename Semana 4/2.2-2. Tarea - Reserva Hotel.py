# Clase que representa un hotel
class Hotel:
    def __init__(self, nombre):
        # Inicializa el hotel con un nombre y una lista vacía de habitaciones
        self.nombre = nombre
        self.habitaciones = []

    # Método para agregar una habitación al hotel
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Método para mostrar habitaciones disponibles en el hotel
    def mostrar_habitaciones_disponibles(self):
        for habitacion in self.habitaciones:
            if habitacion.disponible:  # Verifica si la habitación está disponible
                print(f"Habitación {habitacion.numero} ({habitacion.tipo}) está disponible por ${habitacion.precio}.")

    # Método para reservar una habitación si está disponible
    def reservar_habitacion(self, numero_habitacion, cliente):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.disponible:  # Busca la habitación por número y disponibilidad
                habitacion.reservar(cliente)  # Realiza la reserva
                return True  # Reserva exitosa
        print(f"No se pudo reservar la habitación {numero_habitacion}, no está disponible.")  # Mensaje si no se puede reservar
        return False  # Reserva fallida


# Clase que representa una habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Inicializa la habitación con número, tipo, precio, disponibilidad y sin reserva asociada
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
        self.reserva = None

    # Método para reservar la habitación
    def reservar(self, cliente):
        if self.disponible:  # Verifica si la habitación está disponible
            self.disponible = False  # Cambia el estado de disponibilidad
            self.reserva = Reserva(self, cliente)  # Asocia una reserva a la habitación
            print(f"Habitación {self.numero} reservada por {cliente.nombre}.")  # Mensaje de éxito
        else:
            print(f"Habitación {self.numero} no está disponible.")  # Mensaje si la habitación ya está ocupada


# Clase que representa un cliente del hotel
class Cliente:
    def __init__(self, nombre, email):
        # Inicializa el cliente con un nombre y un correo electrónico
        self.nombre = nombre
        self.email = email


# Clase que representa una reserva de una habitación
class Reserva:
    def __init__(self, habitacion, cliente):
        # Inicializa la reserva con una habitación, un cliente y un estado de confirmación
        self.habitacion = habitacion
        self.cliente = cliente
        self.confirmada = False

    # Método para confirmar la reserva
    def confirmar(self):
        self.confirmada = True  # Cambia el estado de confirmación
        print(f"Reserva para {self.cliente.nombre} en habitación {self.habitacion.numero} confirmada.")  # Mensaje de confirmación


# Crear un hotel de lujo
hotel = Hotel("Hotel Lujo")

# Agregar 40 habitaciones al hotel
for i in range(1, 41):  # Itera desde el 1 hasta el 40
    tipo = "Suite" if i % 2 == 0 else "Deluxe"  # Alterna entre "Suite" y "Deluxe" según el número
    precio = 500 if tipo == "Suite" else 300  # Define el precio según el tipo de habitación
    hotel.agregar_habitacion(Habitacion(i, tipo, precio))  # Crea y agrega la habitación al hotel

# Crear un cliente VIP
cliente_vip = Cliente("Cliente VIP", "andres@gmail.com")

# Mostrar habitaciones disponibles antes de la reserva
print("\nHabitaciones disponibles antes de la reserva:")
hotel.mostrar_habitaciones_disponibles()

# Realizar una reserva para el cliente VIP
if hotel.reservar_habitacion(1, cliente_vip):  # Intenta reservar la habitación número 1
    print("\nReserva realizada con éxito.")

# Mostrar habitaciones disponibles después de la reserva
print("\nHabitaciones disponibles después de la reserva:")
hotel.mostrar_habitaciones_disponibles()
