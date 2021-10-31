class Transporte:
    def Avanzar(self):
        print("Avanzar")

    def Frenar(self):
        pass

    def Sonido(self):
        pass


class Avion(Transporte):
    def Avanzar(self):
        print("Fiiiium")

    def Frenar(self):
        print("Trrrrrr")


class Caballo(Transporte):
    def Avanzar(self):
        print("Yija!")

    def Frenar(self):
        print("Hue quieto!")


class Auto(Transporte):
    def Avanzar(self):
        print("Soy Franchesco!")

    def Frenar(self):
        print("Fiiiiiiiiium")


class Bicicleta(Transporte):
    pass


miAuto = Auto()
miCaballo = Caballo()
miAvion = Avion()
miBici = Bicicleta()
garage = [miAuto, miCaballo, miAvion, miBici]

for i in garage:
    i.Avanzar()
