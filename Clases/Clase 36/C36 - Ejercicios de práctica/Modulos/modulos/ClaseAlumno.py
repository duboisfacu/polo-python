from modulos.ClasePersona import Persona


class Alumno(Persona):
    def saludo(self):
        print(
            f"Hola, soy alumno, mi nombre es {self.nombre} y mi edad es {self.edad}")
