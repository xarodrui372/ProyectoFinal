# Sistema de Gestión de Biblioteca

Aplicación desarrollada en Python para la gestión integral de una biblioteca, aplicando Programación Orientada a Objetos (POO), modularización en paquetes y persistencia de datos en formato JSON. Proyecto final para el ciclo formativo de Grado Superior en Desarrollo de Aplicaciones Web (DAW).

## Funcionalidades Principales
- **Gestión de Libros:** Registro de nuevos libros, control de unicidad por ISBN, listado completo y búsquedas por título o disponibilidad.
- **Gestión de Usuarios:** Registro de usuarios asegurando identificadores únicos.
- **Préstamos y Devoluciones:** Lógica de negocio avanzada que controla el estado de disponibilidad de los ejemplares, verificación de la existencia de usuarios/libros y registro de fechas (con control de préstamos activos).
- **Consultas Especiales:** Visualización de préstamos activos y filtrado de préstamos por usuario.
- **Persistencia de Datos:** Guardado automático y recuperación de la información (libros, usuarios y préstamos) mediante ficheros JSON.
- **Gestión de Errores:** Control robusto de excepciones ante ficheros no encontrados, duplicidades u operaciones no permitidas.

## Estructura del Proyecto

biblioteca/
├── main.py                 # Punto de entrada y gestión del menú de consola
├── modelos/
│   ├── __init__.py
│   ├── libro.py            # Clase Libro y serialización a diccionario
│   ├── usuario.py          # Clase Usuario y serialización a diccionario
│   └── prestamo.py         # Clase Prestamo, propiedades y fechas
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py       # Lógica central del sistema (CRUD, búsquedas, persistencia)
├── datos/
│   ├── libros.json         # Almacenamiento persistente de libros
│   ├── usuarios.json       # Almacenamiento persistente de usuarios
│   └── prestamos.json      # Almacenamiento persistente de préstamos
├── README.md
├── .gitignore
└── requirements.txt