from modulos.ClaseAlumno import Alumno
from modulos.PedirDatos import PedirDatos

PedirDatos = PedirDatos()
nombre, edad = PedirDatos.obtenerDatos()

alumno = Alumno(nombre, edad)
alumno.saludo()
