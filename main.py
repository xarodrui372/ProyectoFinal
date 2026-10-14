from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuarios import Usuario
from servicios.biblioteca import Biblioteca

def mostrar_menu():
    print()
    print("=================================")
    print("     GESTIÓN DE BIBLIOTECA       ")
    print("=================================")

    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")

#Método para opción 1
def registrar_libro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Titulo: ").strip().upper()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Género: ").strip()
    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.registrar_libro(libro)

#Método para opción 2
def registrar_usuario(biblioteca):
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    usuario = Usuario(id, nombre, apellidos, email)
    biblioteca.registrar_usuario(usuario)

#Método para opción 3
def buscar_libro(biblioteca):
    isbn = input("Introduce el isbn del libro que deseas buscar: ").strip().upper()
    biblioteca.buscar_libroNom(isbn)

#Método para opción 4
def listar_libros(biblioteca):
    biblioteca.listar_libros()

#Método para opción 5
def realizar_prestamo(biblioteca):
    id_usuario = int(input("Introduce tu id: "))
    titulo = input("Introduce el nombre del libro que deseas recibir el prestamo: ").strip().upper()
    biblioteca.realizar_prestamo(id_usuario, titulo)

def main():

    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            registrar_libro(biblioteca)
        elif opcion == '2':
            registrar_usuario(biblioteca)
        elif opcion == '3':
            buscar_libro(biblioteca)
        elif opcion == '4':
            listar_libros(biblioteca)
        elif opcion == '5':
            realizar_prestamo(biblioteca)
        elif opcion == '6':
            pass
        elif opcion == '7':
            pass
        elif opcion == '8':
            pass
        elif opcion == '9':
            pass
        elif opcion == '0':
            break
        else:
            print("Opcion incorrecta. Introduce un número del 0 al 9")        

if __name__ == "__main__":
    main()