class DatabaseConnection:
    def __init__(self, db_name):
        """
        Constructor de la clase DatabaseConnection.
        Inicializa la conexión a la base de datos.

        Args:
            db_name (str): Nombre de la base de datos a la que se conectará.
        """
        self.db_name = db_name
        self.connection = self.connect_to_db()
        print(f"Conexión a la base de datos '{self.db_name}' establecida.")
    def connect_to_db(self):
        """
        Simula la conexión a la base de datos.

        Returns:
            str: Cadena simulada de una conexión de base de datos.
        """
        # Aquí iría la lógica real de conexión a la base de datos
        return f"Conexión a {self.db_name}"

def __del__(self):
    """
    Destructor de la clase DatabaseConnection.
    Cierra la conexión a la base de datos.
    """
    self.close_connection()
    print(f"Conexión a la base de datos '{self.db_name}' cerrada.")

def close_connection(self):
 """
Simula el cierre de la conexión a la base de datos.
"""
# Aquí iría la lógica real de cierre de conexión de la base de datos
 self.connection = None

# Uso de la clase DatabaseConnection
if __name__ == "__main__":
    # Crear una instancia de DatabaseConnection
    db = DatabaseConnection("mi_base_de_datos")

# Eliminar la instancia explícitamente para activar el destructor
del db

# Al salir del bloque, el destructor se activará automáticamente si hay instancias no eliminadas
print("Fin del programa.")

