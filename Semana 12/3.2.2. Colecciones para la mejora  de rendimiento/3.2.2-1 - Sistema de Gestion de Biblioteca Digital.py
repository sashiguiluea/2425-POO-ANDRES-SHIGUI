import json  # Importamos el módulo json para manejar la serialización y deserialización de datos en formato JSON.

# Clase Libro
class Libro:
    # Constructor de la clase Libro
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.info = (isbn, titulo, autor)  # Tupla para atributos inmutables (ISBN, título y autor).
        self.categoria = categoria  # Almacena la categoría del libro.
        self.prestado = prestado  # Indica si el libro está prestado o no (por defecto es False).

    # Método que convierte el objeto Libro en un diccionario para facilitar su serialización.
    def to_dict(self):
        return {
            "isbn": self.info[0],  # ISBN del libro.
            "titulo": self.info[1],  # Título del libro.
            "autor": self.info[2],  # Autor del libro.
            "categoria": self.categoria,  # Categoría del libro.
            "prestado": self.prestado  # Estado de préstamo del libro.
        }

# Clase Usuario
class Usuario:
    # Constructor de la clase Usuario
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario  # ID único del usuario.
        self.nombre = nombre  # Nombre del usuario.
        self.libros_prestados = []  # Lista que almacena los libros prestados al usuario.

    # Método que convierte el objeto Usuario en un diccionario para facilitar su serialización.
    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,  # ID del usuario.
            "nombre": self.nombre,  # Nombre del usuario.
            "libros_prestados": [libro.info[0] for libro in self.libros_prestados]  # Lista de ISBN de libros prestados.
        }

# Clase Biblioteca
class Biblioteca:
    # Constructor de la clase Biblioteca
    def __init__(self, archivo_libros='biblioteca.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros  # Nombre del archivo donde se almacenan los libros.
        self.archivo_usuarios = archivo_usuarios  # Nombre del archivo donde se almacenan los usuarios.
        self.libros = self.cargar_libros()  # Carga los libros desde el archivo.
        self.usuarios = self.cargar_usuarios()  # Carga los usuarios desde el archivo.

    # Método que carga los libros desde el archivo JSON.
    def cargar_libros(self):
        try:
            with open(self.archivo_libros, 'r') as archivo:  # Intenta abrir el archivo en modo lectura.
                datos_libros = json.load(archivo)  # Carga los datos del archivo JSON.
                # Crea un diccionario de libros usando el ISBN como clave y el objeto Libro como valor.
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o hay un error en el formato JSON, retorna un diccionario vacío.
            return {}

    # Método que guarda los libros en el archivo JSON.
    def guardar_libros(self):
        with open(self.archivo_libros, 'w') as archivo:  # Abre el archivo en modo escritura.
            # Convierte los libros a un diccionario y los guarda en formato JSON.
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    # Método que carga los usuarios desde el archivo JSON.
    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'r') as archivo:  # Intenta abrir el archivo en modo lectura.
                datos_usuarios = json.load(archivo)  # Carga los datos del archivo JSON.
                usuarios = {}  # Diccionario para almacenar los usuarios.
                for id_usuario, datos in datos_usuarios.items():  # Estructura de control: bucle for para iterar sobre los usuarios.
                    # Crea un objeto Usuario y asigna los libros prestados si están disponibles.
                    usuario = Usuario(datos["id_usuario"], datos["nombre"])
                    usuario.libros_prestados = [self.libros[isbn] for isbn in datos["libros_prestados"] if isbn in self.libros]
                    usuarios[id_usuario] = usuario  # Agrega el usuario al diccionario.
                return usuarios  # Retorna el diccionario de usuarios.
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o hay un error en el formato JSON, retorna un diccionario vacío.
            return {}

    # Método que guarda los usuarios en el archivo JSON.
    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as archivo:  # Abre el archivo en modo escritura.
            # Convierte los usuarios a un diccionario y los guarda en formato JSON.
            json.dump({id_usuario: usuario.to_dict() for id_usuario, usuario in self.usuarios.items()}, archivo, indent=4)

    # Método para añadir un nuevo libro a la biblioteca.
    def añadir_libro(self):
        isbn = input("Ingrese ISBN: ")  # Solicita el ISBN del libro.
        if isbn in self.libros:  # Estructura de control: verifica si el libro ya está registrado.
            print("Este libro ya está registrado.")
            return  # Sale del método si el libro ya existe.
        titulo = input("Ingrese título: ")  # Solicita el título del libro.
        autor = input("Ingrese autor: ")  # Solicita el autor del libro.
        categoria = input("Ingrese categoría: ")  # Solicita la categoría del libro.
        libro = Libro(isbn, titulo, autor, categoria)  # Crea un nuevo objeto Libro.
        self.libros[isbn] = libro  # Agrega el libro al diccionario de libros.
        self.guardar_libros()  # Guarda los cambios en el archivo.

    # Método para registrar un nuevo usuario en la biblioteca.
    def registrar_usuario(self):
        id_usuario = input("Ingrese ID de usuario: ")  # Solicita el ID del usuario.
        if id_usuario in self.usuarios:  # Estructura de control: verifica si el usuario ya está registrado.
            print("El usuario ya está registrado.")
            return  # Sale del método si el usuario ya existe.
        nombre = input("Ingrese nombre del usuario: ")  # Solicita el nombre del usuario.
        usuario = Usuario(id_usuario, nombre)  # Crea un nuevo objeto Usuario.
        self.usuarios[id_usuario] = usuario  # Agrega el usuario al diccionario de usuarios.
        self.guardar_usuarios()  # Guarda los cambios en el archivo.

    # Método para prestar un libro a un usuario.
    def prestar_libro(self):
        id_usuario = input("Ingrese ID de usuario: ")  # Solicita el ID del usuario.
        isbn = input("Ingrese ISBN del libro a prestar: ")  # Solicita el ISBN del libro a prestar.
        if id_usuario not in self.usuarios:  # Estructura de control: verifica si el usuario está registrado.
            print("Usuario no registrado.")
            return  # Sale del método si el usuario no existe.
        if isbn not in self.libros or self.libros[isbn].prestado:  # Estructura de control: verifica si el libro está disponible.
            print("Libro no disponible para préstamo.")
            return  # Sale del método si el libro no está disponible.
        self.libros[isbn].prestado = True  # Marca el libro como prestado.
        self.usuarios[id_usuario].libros_prestados.append(self.libros[isbn])  # Agrega el libro a la lista de libros prestados del usuario.
        self.guardar_libros()  # Guarda los cambios en el archivo de libros.
        self.guardar_usuarios()  # Guarda los cambios en el archivo de usuarios.
        print(f"Libro {isbn} prestado con éxito.")  # Mensaje de éxito.

    # Método para devolver un libro prestado por un usuario.
    def devolver_libro(self):
        id_usuario = input("Ingrese ID de usuario: ")  # Solicita el ID del usuario.
        isbn = input("Ingrese ISBN del libro a devolver: ")  # Solicita el ISBN del libro a devolver.
        if id_usuario not in self.usuarios:  # Estructura de control: verifica si el usuario está registrado.
            print("Usuario no registrado.")
            return  # Sale del método si el usuario no existe.
        usuario = self.usuarios[id_usuario]  # Obtiene el objeto Usuario.
        for libro in usuario.libros_prestados:  # Estructura de control: bucle for para iterar sobre los libros prestados por el usuario.
            if libro.info[0] == isbn:  # Verifica si el libro a devolver está en la lista de libros prestados.
                usuario.libros_prestados.remove(libro)  # Elimina el libro de la lista de libros prestados.
                self.libros[isbn].prestado = False  # Marca el libro como disponible.
                self.guardar_libros()  # Guarda los cambios en el archivo de libros.
                self.guardar_usuarios()  # Guarda los cambios en el archivo de usuarios.
                print(f"Libro {isbn} devuelto con éxito.")  # Mensaje de éxito.
                return  # Sale del método.
        print("El usuario no tiene prestado este libro.")  # Mensaje si el libro no estaba prestado por el usuario.

    # Método para mostrar todos los libros en la biblioteca.
    def mostrar_libros(self):
        for libro in self.libros.values():  # Estructura de control: bucle for para iterar sobre todos los libros.
            estado = "Prestado" if libro.prestado else "Disponible"  # Determina el estado del libro.
            print(f"{libro.info[0]}: {libro.info[1]} por {libro.info[2]} - {estado}")  # Muestra la información del libro.

    # Método para buscar libros por título, autor o categoría.
    def buscar_libro(self):
        criterio = input("Ingrese título, autor o categoría para buscar: ").lower()  # Solicita el criterio de búsqueda.
        # Filtra los libros que coinciden con el criterio en título, autor o categoría.
        resultados = [libro for libro in self.libros.values() if criterio in libro.info[1].lower() or criterio in libro.info[2].lower() or criterio in libro.categoria.lower()]
        for libro in resultados:  # Estructura de control: bucle for para iterar sobre los resultados encontrados.
            print(f"{libro.info[0]}: {libro.info [1]} por {libro.info[2]} - {'Prestado' if libro.prestado else 'Disponible'}")  # Muestra la información de los libros encontrados.

    # Método para listar los libros prestados a un usuario específico.
    def listar_libros_prestados(self):
        id_usuario = input("Ingrese ID de usuario: ")  # Solicita el ID del usuario.
        if id_usuario not in self.usuarios:  # Estructura de control: verifica si el usuario está registrado.
            print("Usuario no registrado.")  # Mensaje si el usuario no existe.
            return  # Sale del método.
        usuario = self.usuarios[id_usuario]  # Obtiene el objeto Usuario.
        if not usuario.libros_prestados:  # Estructura de control: verifica si el usuario no tiene libros prestados.
            print("El usuario no tiene libros prestados.")  # Mensaje si no hay libros prestados.
            return  # Sale del método.
        for libro in usuario.libros_prestados:  # Estructura de control: bucle for para iterar sobre los libros prestados por el usuario.
            print(f"{libro.info[0]}: {libro.info[1]} por {libro.info[2]}")  # Muestra la información de los libros prestados.

# Función principal que muestra el menú de opciones para interactuar con la biblioteca.
def menu():
    biblioteca = Biblioteca()  # Crea una instancia de la clase Biblioteca.
    while True:  # Estructura de control: bucle infinito para mostrar el menú hasta que el usuario decida salir.
        print("\n1. Añadir Libro\n2. Registrar Usuario\n3. Prestar Libro\n4. Devolver Libro\n5. Mostrar Libros\n6. Buscar Libro\n7. Listar Libros Prestados\n8. Salir")  # Opciones del menú.
        opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción.
        if opcion == '1':  # Opción para añadir un libro.
            biblioteca.añadir_libro()
        elif opcion == '2':  # Opción para registrar un usuario.
            biblioteca.registrar_usuario()
        elif opcion == '3':  # Opción para prestar un libro.
            biblioteca.prestar_libro()
        elif opcion == '4':  # Opción para devolver un libro.
            biblioteca.devolver_libro()
        elif opcion == '5':  # Opción para mostrar todos los libros.
            biblioteca.mostrar_libros()
        elif opcion == '6':  # Opción para buscar un libro.
            biblioteca.buscar_libro()
        elif opcion == '7':  # Opción para listar libros prestados a un usuario.
            biblioteca.listar_libros_prestados()
        elif opcion == '8':  # Opción para salir del sistema.
            print("Saliendo del sistema...")  # Mensaje de salida.
            break  # Sale del bucle y termina el programa.
        else:  # Opción no válida.
            print("Opción no válida. Intente de nuevo.")  # Mensaje de error.

if __name__ == "__main__":
    menu()  # Llama a la función menu para iniciar el programa.