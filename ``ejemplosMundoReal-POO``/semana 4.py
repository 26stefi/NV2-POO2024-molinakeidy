# Clase Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(f'Habitación {habitacion.numero} ({habitacion.tipo}) está disponible por ${habitacion.precio}.')

    def reservar_habitacion(self, numero_habitacion, cliente):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.disponible:
                habitacion.reservar(cliente)
                return True
        return False


# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
        self.reserva = None

    def reservar(self, cliente):
        if self.disponible:
            self.disponible = False
            self.reserva = Reserva(self, cliente)
            print(f'Habitación {self.numero} reservada por {cliente.nombre}.')
        else:
            print(f'Habitación {self.numero} no está disponible.')


# Clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# Clase Reserva
class Reserva:
    def __init__(self, habitacion, cliente):
        self.habitacion = habitacion
        self.cliente = cliente
        self.confirmada = False

    def confirmar(self):
        self.confirmada = True
        print(f'Reserva para {self.cliente.nombre} en habitación {self.habitacion.numero} confirmada.')
        from hotel import Hotel
        from habitacion import Habitacion
        from cliente import Cliente


# Crear un hotel de lujo
hotel = Hotel("Hotel de Lujo")

# Agregar 40 habitaciones al hotel
for i in range(1, 41):
    tipo = "Suite" if i % 2 == 0 else "Deluxe"
    precio = 500 if tipo == "Suite" else 300
    hotel.agregar_habitacion(Habitacion(i, tipo, precio))

# Crear un cliente VIP
cliente_vip = Cliente("Cliente VIP", "vip@example.com")

# Mostrar habitaciones disponibles antes de la reserva
hotel.mostrar_habitaciones_disponibles()

# Realizar tres reservas para el cliente VIP
reservas_realizadas = 0
for i in range(1, 41):
    if hotel.reservar_habitacion(i, cliente_vip):
        reservas_realizadas += 1
        if reservas_realizadas == 3:
            break

# Mostrar habitaciones disponibles después de las reservas
hotel.mostrar_habitaciones_disponibles()