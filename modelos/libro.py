class Libro:
    def __init__(self, isbn, titulo, autor, genero, anio = None, disponible = True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio = anio
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn}\nTitulo: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}\nAnio: {self.anio}\nDisponible: {estado}"

    def __repr__(self):
        return (
            f"Libro(isbn={self.isbn!r})"
            f"titulo={self.titulo!r}"
            f"autor={self.autor!r}"
            f"anio={self.anio!r}"
            f"disponible={self.disponible!r}"
        )

    def __eq__(self, _value):
        return self.isbn == _value.isbn
