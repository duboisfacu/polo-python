from ClasePersona import Persona


class Alumno(Persona):
    turno = ""
    grado = ""

    def saludo(self):
        print(
            f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años y asisto al turno {self.turno}.')
