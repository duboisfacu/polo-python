import datetime as dt


class PedirDatos:
    def __init__(self):
        pass

    def obtenerDatos(self):
        nombre = input("Nombre: ")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))

        fechaNacimiento = dt.date(anio, mes, dia)
        fechaActual = dt.date.today()
        diasVividos = fechaActual - fechaNacimiento
        edad = int(diasVividos.days / 365)
        return (nombre, edad)
