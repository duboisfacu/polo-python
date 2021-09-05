class Vehiculo:
    marca = "Reault"

    def __init__(self,mod):
        self.modelo = mod

auto1 = Vehiculo("207")
auto2 = Vehiculo("208")
auto3 = Vehiculo("104")

auto2.marca = Vehiculo.marca
print(auto1.modelo)
print(auto2.modelo)
print(auto3.modelo)

Vehiculo.marca = "Peugeot"

print(auto1.marca)
print(auto2.marca)
print(auto3.marca)