class Vehiculo:

    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.anio = 0

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        print("Vehículo creado satisfactoriamente.")


def NuevoVehiculo(mensaje):
    Dato = input(mensaje)
    NuevoVehiculo.Salir = False
    if Dato == "SALIR":
        NuevoVehiculo.Salir = True
    Actual.append(Dato)


VehiculoData = []
MSGArr = ["Ingrese la marca: ", "Ingrese el modelo: ", "Ingrese el año: "]
VALArr = ["marca", "modelo", "año"]
Vehiculos = []


while True:
    print("---------------------------------")
    caca = (input("Deseas cargar un nuevo Vehiculo? (Y/N): ").upper())
    if caca == "Y":
        print("Para cancelar escriba 'SALIR'")
        print("---------------------------------")
        Actual = []
        for msg in range(len(MSGArr)):
            NuevoVehiculo(MSGArr[msg])
            if NuevoVehiculo.Salir == True:
                break
        if NuevoVehiculo.Salir == True:

            break
        Marca = Actual[0]
        Modelo = Actual[1]
        Anio = Actual[2]
        Vehiculos.append(Vehiculo(Marca, Modelo, Anio))
    else:
        break
if len(Vehiculos) > 0:
    print("Vehículos Cargados:")
    for i in range(len(Vehiculos)):
        print(
            f'{i + 1}) Vehículo: {Vehiculos[i].marca}, año: {Vehiculos[i].anio}')
else:
    print("No hay vehículos cargados.")
