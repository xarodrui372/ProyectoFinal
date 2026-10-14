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

def registrar_libro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Género: ").strip()
    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.registrar_libro(libro)

def main():

    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            registrar_libro(biblioteca)
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
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