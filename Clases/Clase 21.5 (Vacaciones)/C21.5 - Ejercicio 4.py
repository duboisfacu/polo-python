#Diseñar un programa que actúe como base de datos de personas. Se le
#presentará al usuario un menú con las opciones para cargar una nueva
#persona, imprimir por pantalla las personas que se hayan cargado, o
#salir del programa.


personas = []

while True:
    opc = input("1) Añadir persona\n2) Mostrar personas\n3) Salir del programa\nElige una opción: ")
    if opc == "1":
        while True:
            add = input("Ingrese el nombre de la persona (volver con 0): ")
            if add == "0":
                break
            personas.append(add)
    if opc == "2":
        print("Las personas cargadas son:\n" + ("\n".join(personas)))
    if opc == "3":
        exit