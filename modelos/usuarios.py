class Usuario:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nEmail: {self.email}"

    def __repr__(self):
        return (
            f"Usuario(id={self.id!r}"
            f"Nombre={self.nombre!r}"
            f"Apellidos={self.apellidos!r}"
            f"Email={self.email!r}"
        )

    def __eq__(self, _value):
        return self.id == _value.id

    #Método para pasar el objeto a diccionario, se usará para escribir en JSON
    def a_diccionario(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email
        }