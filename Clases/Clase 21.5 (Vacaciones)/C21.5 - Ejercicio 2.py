#Diseñar un programa que pida al usuario un
#número entero, y utilice dicho número para generar una escalera de
#asteriscos (*). Por ejemplo, si el usuario ingresa un 5, la salida por
#pantalla debe ser la siguiente:

#*
#**
#***
#****
#*****
# Solicitar al usuario si desea imprimir la escalera de forma invertida.

num = int(input("Ingrese un número: "))
ateriscos = ""


for x in range(num):
    ateriscos += "*"
    print(ateriscos)

ateriscosinvertidos = ateriscos
invertida = (input("Deseas invertir la escalera? \n(si/no): "))

if invertida == "si":
    for x in range(num):
        print(ateriscosinvertidos)
        ateriscosinvertidos = ateriscosinvertidos[:-1]
    