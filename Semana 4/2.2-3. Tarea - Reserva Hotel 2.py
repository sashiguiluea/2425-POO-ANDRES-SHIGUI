# Clase que representa una habitación en el hotel
class Room:
    def __init__(self, number, room_type, price_per_night):
        # Constructor para inicializar los atributos principales de la habitación
        self.number = number  # Número único de la habitación
        self.room_type = room_type  # Tipo de habitación (por ejemplo: 'Single', 'Double', 'Suite')
        self.price_per_night = price_per_night  # Precio por noche
        self.is_available = True  # Estado inicial de disponibilidad (True: disponible)

    def __str__(self):
        # Método especial para generar una representación legible de la habitación
        status = "Disponible" if self.is_available else "Ocupada"  # Determina el estado de la habitación
        return f"Habitación {self.number} ({self.room_type}) - ${self.price_per_night}/noche - {status}"


# Clase que representa una reserva en el hotel
class Reservation:
    def __init__(self, reservation_id, guest_name, room, check_in, check_out):
        # Constructor para inicializar los atributos principales de una reserva
        self.reservation_id = reservation_id  # Identificador único de la reserva
        self.guest_name = guest_name  # Nombre del huésped que realizó la reserva
        self.room = room  # Objeto que representa la habitación reservada
        self.check_in = check_in  # Fecha de inicio de la reserva
        self.check_out = check_out  # Fecha de fin de la reserva

    def __str__(self):
        # Método especial para generar una representación legible de la reserva
        return (f"Reserva {self.reservation_id}: {self.guest_name} - "
                f"Habitación {self.room.number} ({self.room.room_type}) - "
                f"Del {self.check_in} al {self.check_out}")


# Clase que representa un hotel con habitaciones y reservas
class Hotel:
    def __init__(self, name):
        # Constructor para inicializar el nombre del hotel, sus habitaciones y reservas
        self.name = name  # Nombre del hotel
        self.rooms = []  # Lista para almacenar los objetos Room
        self.reservations = {}  # Diccionario para almacenar las reservas (clave: ID de la reserva)

    # Método para agregar una habitación al hotel
    def add_room(self, room):
        self.rooms.append(room)  # Agrega la habitación proporcionada a la lista de habitaciones

    # Método para listar todas las habitaciones del hotel
    def list_rooms(self):
        print("Estado de las habitaciones:")  # Muestra un encabezado
        for room in self.rooms:  # Itera sobre todas las habitaciones
            print(room)  # Muestra la información de cada habitación usando su método __str__

    # Método para listar las habitaciones disponibles
    def list_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.is_available]
        # Filtra solo las habitaciones disponibles
        if available_rooms:  # Verifica si hay habitaciones disponibles
            print("Habitaciones disponibles:")
            for room in available_rooms:  # Itera sobre las habitaciones disponibles
                print(room)  # Muestra su información
        else:
            print("No hay habitaciones disponibles.")  # Mensaje si todas las habitaciones están ocupadas

    # Método para realizar una reserva
    def make_reservation(self, guest_name, room_number, check_in, check_out):
        room = next((room for room in self.rooms if room.number == room_number), None)
        # Busca la habitación por su número
        if room and room.is_available:  # Verifica que la habitación exista y esté disponible
            reservation_id = len(self.reservations) + 1  # Genera un nuevo ID de reserva
            reservation = Reservation(reservation_id, guest_name, room, check_in, check_out)
            # Crea el objeto de reserva
            self.reservations[reservation_id] = reservation  # Almacena la reserva en el diccionario
            room.is_available = False  # Marca la habitación como ocupada
            print(f"Reserva exitosa: {reservation}")  # Mensaje de éxito
        else:
            print(f"Habitación {room_number} no está disponible o no existe.")
            # Mensaje si la habitación no está disponible o no existe

    # Método para cancelar una reserva
    def cancel_reservation(self, reservation_id):
        reservation = self.reservations.pop(reservation_id, None)  # Elimina la reserva del diccionario
        if reservation:  # Si la reserva existe
            reservation.room.is_available = True  # Marca la habitación asociada como disponible
            print(f"Reserva {reservation_id} cancelada exitosamente.")  # Mensaje de éxito
        else:
            print("Reserva no encontrada.")  # Mensaje si no se encontró la reserva

    # Método para listar todas las reservas actuales
    def list_reservations(self):
        if self.reservations:  # Verifica si hay reservas
            print("Reservas actuales:")
            for reservation in self.reservations.values():  # Itera sobre todas las reservas
                print(reservation)  # Muestra la información de cada reserva
        else:
            print("No hay reservas.")  # Mensaje si no hay reservas
# Uso del sistema

# Crear un hotel
hotel = Hotel("Hotel Ambato")

# Agregar habitaciones al hotel
hotel.add_room(Room(101, "Single", 50))
hotel.add_room(Room(102, "Double", 80))
hotel.add_room(Room(201, "Suite", 150))

# Mostrar el estado inicial de las habitaciones
print("\n--- Estado inicial de las habitaciones ---")
hotel.list_rooms()

# Realizar reservas
print("\n--- Realizando reservas ---")
hotel.make_reservation("Alice", 101, "2025-01-15", "2025-01-20")
hotel.make_reservation("Bob", 201, "2025-01-18", "2025-01-25")

# Mostrar el estado de las habitaciones después de las reservas
print("\n--- Estado de las habitaciones después de las reservas ---")
hotel.list_rooms()

# Cancelar una reserva
print("\n--- Cancelar una reserva ---")
hotel.cancel_reservation(1)

# Mostrar el estado final de las habitaciones
print("\n--- Estado final de las habitaciones ---")
hotel.list_rooms()

# Mostrar las reservas finales
print("\n--- Reservas finales ---")
hotel.list_reservations()
