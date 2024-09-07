# Clase Libro: Representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


# Clase Usuario: Representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca: Gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: ISBN -> Libro
        self.usuarios = {}  # Diccionario: ID_usuario -> Usuario
        self.libros_prestados = {}  # Diccionario: ISBN -> ID_usuario (libros actualmente prestados)

    # Añadir un libro
    def anadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    # Quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            if isbn in self.libros_prestados:
                print(f"El libro con ISBN {isbn} está prestado y no se puede quitar.")
            else:
                libro = self.libros.pop(isbn)
                print(f"Libro '{libro.titulo}' ha sido eliminado de la biblioteca.")
        else:
            print(f"No existe un libro con ISBN {isbn} en la biblioteca.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"El usuario tiene libros prestados y no se puede dar de baja.")
            else:
                self.usuarios.pop(id_usuario)
                print(f"Usuario '{usuario.nombre}' ha sido dado de baja.")
        else:
            print(f"No existe un usuario con ID {id_usuario} registrado.")

    # Prestar un libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros:
            print(f"No existe un libro con ISBN {isbn} en la biblioteca.")
        elif isbn in self.libros_prestados:
            print(f"El libro con ISBN {isbn} ya está prestado.")
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            self.libros_prestados[isbn] = id_usuario
            print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")

    # Devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros_prestados or self.libros_prestados[isbn] != id_usuario:
            print(f"El libro con ISBN {isbn} no está prestado a este usuario.")
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.remove(libro)
            del self.libros_prestados[isbn]
            print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")

    # Buscar libros
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and libro.titulo.lower() == valor.lower()) or \
                    (criterio == "autor" and libro.autor.lower() == valor.lower()) or \
                    (criterio == "categoria" and libro.categoria.lower() == valor.lower()):
                resultados.append(libro)
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros por {criterio}: {valor}")

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"El usuario '{usuario.nombre}' no tiene libros prestados.")
        else:
            print(f"No existe un usuario con ID {id_usuario} registrado.")


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "1234567890")
    libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "0987654321")

    # Añadir libros a la biblioteca
    biblioteca.anadir_libro(libro1)
    biblioteca.anadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana García", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", "1234567890")
    biblioteca.prestar_libro("002", "0987654321")

    # Listar libros prestados a un usuario
    biblioteca.listar_libros_prestados("001")

    # Devolver libros
    biblioteca.devolver_libro("001", "1234567890")

    # Buscar libros por título
    biblioteca.buscar_libro("titulo", "El Quijote")