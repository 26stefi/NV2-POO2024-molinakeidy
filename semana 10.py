import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}'


class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_inventario_desde_archivo()

    def cargar_inventario_desde_archivo(self):
        """Carga productos desde un archivo al iniciar el programa."""
        try:
            with open("inventario.txt", "r") as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(", ")
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado desde archivo con éxito.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Permiso denegado para leer el archivo de inventario.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")

    def guardar_inventario_en_archivo(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open("inventario.txt", "w") as file:
                for producto in self.productos:
                    file.write(
                        f"{producto.get_id()}, {producto.get_nombre()}, {producto.get_cantidad()}, {producto.get_precio()}\n")
            print("Inventario guardado en archivo con éxito.")
        except PermissionError:
            print("Permiso denegado para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto y lo guarda en el archivo."""
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            self.guardar_inventario_en_archivo()
            print(f'Producto {producto.get_nombre()} añadido con éxito.')
        else:
            print(f'Error: Ya existe un producto con el ID {producto.get_id()}.')

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID y actualiza el archivo."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario_en_archivo()
                print(f'Producto con ID {id_producto} eliminado con éxito.')
                return
        print(f'Error: No se encontró un producto con el ID {id_producto}.')

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza un producto por su ID y guarda los cambios en el archivo."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario_en_archivo()
                print(f'Producto con ID {id_producto} actualizado con éxito.')
                return
        print(f'Error: No se encontró un producto con el ID {id_producto}.')

    def buscar_producto_por_nombre(self, nombre):
        """Busca productos por nombre y muestra los resultados."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print(f'Se encontraron {len(resultados)} resultado(s) para "{nombre}":')
            for producto in resultados:
                print(producto)
        else:
            print(f'No se encontraron productos con el nombre "{nombre}".')

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            print('Lista de productos en el inventario:')
            for producto in self.productos:
                print(producto)
        else:
            print('El inventario está vacío.')


def menu():
    inventario = Inventario()

    # Añadir productos iniciales al inventario
    producto1 = Producto("0L1", "beautiful-nails largas", 30, 10.00)
    producto2 = Producto("m2s", "beautiful-nails medianas", 30, 15.00)
    producto3 = Producto("3ps", "beautiful-nails pequeñas", 30, 20.00)

    # Asegurar que estos productos no se dupliquen al reiniciar el programa
    if not any(p.get_id() == producto1.get_id() for p in inventario.productos):
        inventario.añadir_producto(producto1)
    if not any(p.get_id() == producto2.get_id() for p in inventario.productos):
        inventario.añadir_producto(producto2)
    if not any(p.get_id() == producto3.get_id() for p in inventario.productos):
        inventario.añadir_producto(producto3)

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto,
                                           cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()