from modelos.libro import Libro
from modelos.prestamo import Prestamo
class Biblioteca:
    def __init__(self):
        self.libros = libros = []
        self.usuarios = usuarios = []
        self.prestamos = prestamos = []

    def registrar_libro(self, libro_nuevo):
        #buscar si hay otro libro con mismo isbn
        if self.buscar_libro(libro_nuevo):
            print('El libro con ese ISBN ya está en la lista')
            return
        self.libros.append(libro_nuevo)

    #Método para buscar libro por ISBN, para posteriormente utilizarlo en el método registrar_libro y comprobar que el libro que se introduce no tiene el mismo ISBN.
    def buscar_libro(self, libro_nuevo):
        for libro in self.libros:
            if libro.__eq__(libro_nuevo):
                return libro
        return None

    def registrar_usuario(self, usuario_nuevo):
        if self.buscar_usuario(usuario_nuevo):
            print('El usuario con ese id ya se encuentra en la lista.')
            return
        self.usuarios.append(usuario_nuevo)

    #Método que busca al usuario por nombre
    def buscar_usuario(self, usuario_nuevo):
        for usuario in self.usuarios:
            if usuario.__eq__(usuario_nuevo):
                return usuario
        return None

    #Método que busca al usuario por id
    def buscar_usuarioID(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id.__eq__(id_usuario):
                return usuario
        return None

    #Método para buscar libro por nombre, se va a usar en la opción 3 del menú.
    def buscar_libroNom(self, titulo_buscado):
        for libro in self.libros:
            if libro.titulo == titulo_buscado:
                print(f"El libro {titulo_buscado} ha sido encontrado.")
                return libro
            else:
                print(f"El libro {titulo_buscado} no ha sido encontrado")
        return None

    #Método para listar todos los libros, se va a usar en la opción 4 del menú.
    def listar_libros(self):
        for i, libro in enumerate(self.libros, start=1):
            print(f"Libro {i}:\n{libro}\n")

    #Método para realizar prestamo, se va a usar en la opción 5 del menú.
    def realizar_prestamo(self, id_buscado, titulo_buscado):
        libro = self.buscar_libroNom(titulo_buscado)
        usuario = self.buscar_usuarioID(id_buscado)
        if usuario is None or libro is None:
            print("El usuario o el libro no existen.")
            return
        if libro.disponible == False:
            print("El libro ya está prestado")
            return
        nuevo_prestamo = Prestamo(usuario, libro)
        self.prestamos.append(nuevo_prestamo)
        libro.disponible = False
        print("Prestamo realizado correctamente")
