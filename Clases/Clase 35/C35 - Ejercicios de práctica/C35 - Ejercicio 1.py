from ClasePersona import Persona
from ClaseAlumno import Alumno

persona1 = Persona()
persona1.nombre = "Juan"
persona1.edad = 17

alumno1 = Alumno()
alumno1.nombre = "Ramiro"
alumno1.edad = 17
alumno1.turno = "Tarde"

persona1.saludo()
alumno1.saludo()
