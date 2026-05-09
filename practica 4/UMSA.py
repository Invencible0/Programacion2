# CLASE AUTOR
class Autor:

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"
# CLASE ESTUDIANTE
class Estudiante:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")

    def __str__(self):
        return f"{self.nombre} [{self.codigo}]"
# CLASE LIBRO
class Libro:
  # CLASE INTERNA PAGINA
    # COMPOSICION
    class Pagina:

        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def __str__(self):
            return f"Pagina {self.numero}: {self.contenido}"

    def __init__(self, titulo, isbn, contenido_paginas):

        self.titulo = titulo
        self.isbn = isbn

        # COMPOSICION
        self.paginas = []

        # El libro CREA sus paginas
        for i, contenido in enumerate(contenido_paginas, start=1):
            pagina = self.Pagina(i, contenido)
            self.paginas.append(pagina)

        print(f"Libro '{self.titulo}' creado correctamente")

    def leer(self):

        print(f"===== LEYENDO {self.titulo} =====")

        for pagina in self.paginas:
            print(pagina)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

    # Si el libro desaparece, tambien desaparecen sus paginas
    def __del__(self):
        print(f"Destruyendo libro '{self.titulo}'")
        self.paginas.clear()
        print("Todas las paginas fueron destruidas")
# CLASE PRESTAMO
# ASOCIACION
class Prestamo:

    def __init__(self, estudiante, libro):

        self.fecha_prestamo = "09/05/2026"
        self.fecha_devolucion = "16/05/2026"

        # ASOCIACION
        self.estudiante = estudiante
        self.libro = libro

        print(f"Prestamo realizado: {libro.titulo} -> {estudiante.nombre}")

    def mostrar_info(self):

        print("=== PRESTAMO ===")
        print(f"Estudiante: {self.estudiante}")
        print(f"Libro: {self.libro}")
        print(f"Fecha prestamo: {self.fecha_prestamo}")
        print(f"Fecha devolucion: {self.fecha_devolucion}")
# CLASE BIBLIOTECA
class Biblioteca:
# CLASE INTERNA HORARIO
    # COMPOSICION
    class Horario:

        def __init__(self, dias, apertura, cierre):
            self.dias = dias
            self.apertura = apertura
            self.cierre = cierre

        def mostrar_horario(self):

            print("=== HORARIO ===")
            print(f"Dias: {self.dias}")
            print(f"Apertura: {self.apertura}")
            print(f"Cierre: {self.cierre}")

        def __str__(self):
            return f"{self.dias} | {self.apertura} - {self.cierre}"

    def __init__(self, nombre):

        self.nombre = nombre

        # AGREGACION
        self.libros = []
        self.autores = []

        self.prestamos = []

        # COMPOSICION
        self.horario = self.Horario(
            "Lunes a Viernes",
            "08:00",
            "20:00"
        )

        print(f"Biblioteca '{self.nombre}' creada correctamente")

    def agregar_libro(self, libro):

        self.libros.append(libro)

        print(f"+ Libro '{libro.titulo}' agregado")

    def agregar_autor(self, autor):

        self.autores.append(autor)

        print(f"+ Autor '{autor.nombre}' registrado")

    def prestar_libro(self, estudiante, libro):

        prestamo = Prestamo(estudiante, libro)

        self.prestamos.append(prestamo)

    def mostrar_estado(self):

        print(f"========== BIBLIOTECA {self.nombre} ==========")

        print("LIBROS")
        for libro in self.libros:
            print("-", libro)

        print("\nAUTORES")
        for autor in self.autores:
            print("-", autor)

        print("PRESTAMOS")
        if len(self.prestamos) == 0:
            print("No existen prestamos")
        else:
            for prestamo in self.prestamos:
                prestamo.mostrar_info()

        self.horario.mostrar_horario()

    def cerrar_biblioteca(self):

        print(f"\nCerrando biblioteca '{self.nombre}'")

        self.prestamos.clear()

        print("Todos los prestamos fueron eliminados")

    # Si la biblioteca desaparece,
    # tambien desaparece su horario
    def __del__(self):

        print(f"Destruyendo biblioteca '{self.nombre}'")

        self.prestamos.clear()

        print("Horario destruido")
        print("Prestamos destruidos")

# MAIN
# Crear biblioteca
biblioteca = Biblioteca("Biblioteca UMSA")

# Crear autores
autor1 = Autor(
    "Gabriel Garcia Marquez",
    "Colombiano"
)

autor2 = Autor(
    "Mario Vargas Llosa",
    "Peruano"
)

# Crear libros
libro1 = Libro(
    "Cien Años de Soledad",
    "ISBN-111",
    [
        "Contenido pagina 1",
        "Contenido pagina 2",
        "Contenido pagina 3"
    ]
)

libro2 = Libro(
    "Python Basico",
    "ISBN-222",
    [
        "Variables y tipos",
        "POO en Python",
        "Herencia y Polimorfismo"
    ]
)

# Crear estudiante
estudiante1 = Estudiante(
    "2025001",
    "Carlos Perez"
)
# AGREGACION
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)
# ASOCIACION
biblioteca.prestar_libro(
    estudiante1,
    libro1
)

# Mostrar estado
biblioteca.mostrar_estado()

# Leer libro
libro1.leer()
# COMPOSICION
biblioteca.cerrar_biblioteca()
# Destruir biblioteca
biblioteca = None
# Destruir libro
libro1 = None