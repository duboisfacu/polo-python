#Crear contador que: 
#al ingresar la opcion 1 sume un valor al valor del archivo 
#al seleccionar la ocion 2 reste un valor al valor del archivo 
#al seleccionar la opcion 3 salga


def DetectarNumero(numero):
    with open("Clases/Clase 24/C24 - Ejercicios de práctica/C24 - Contador.txt", "r") as Abrir:
        Nuevo = (int(Abrir.read()) + numero)
    with open("Clases/Clase 24/C24 - Ejercicios de práctica/C24 - Contador.txt", "w") as Abrir:
        Abrir.write(str(Nuevo))
        return print("Listo!")

while True:
    opcion = (input("----------------------------\nBienvenido!\n1)Aumenta 1 número\n2)Disminuye un número\n3)Salir\nElige una opción: "))

    if opcion.isnumeric():
        if opcion == "1":
            DetectarNumero(1)
            continue
        elif opcion =="2":
            DetectarNumero(-1)
            continue
        elif opcion =="3":
            break
        else:
            print("Valor incorrecto")
    else:
        print("Valor incorrecto")