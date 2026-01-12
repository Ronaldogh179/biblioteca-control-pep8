"""Script principal del sistema de biblioteca."""
from biblioteca import Biblioteca, Libro

biblioteca = Biblioteca("central")

libro1 = Libro("Python", "Guido", 1)
libro2 = Libro("Java", "Gosling", 2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

print(libro1.prestar())
print(libro1.prestar())
libro1.devolver()
print(libro1.prestar())
