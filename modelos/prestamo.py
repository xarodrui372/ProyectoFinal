from datetime import date

class Prestamo:
    def __init__(self, Usuario, Libro, fecha_prestamo = None, fecha_devolucion = None):
        self.Usuario = Usuario
        self.Libro = Libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __str__(self):
        estado = "Activo" if self.activo else f"Devuelto: {self.fecha_devolucion}"
        return f"Prestamo realizado por: {self.Usuario.nombre}, {self.Usuario.apellidos}\nLibro:{self.Libro.titulo}\nFecha_prestamo:{self.fecha_prestamo}\nEstado:{estado}"

    #Método para pasar el objeto a diccionario, se usará para escribir en JSON
    def a_diccionario(self):
        return{
            "Usuario": self.Usuario.id,
            "Libro": self.Libro.titulo,
            "fecha_prestamo": str(self.fecha_prestamo),
            "fecha_devolucion": (str(self.fecha_devolucion) if self.fecha_devolucion is not None else None)
        }