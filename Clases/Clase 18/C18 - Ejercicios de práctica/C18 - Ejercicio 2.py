#Crear una calculadora básica que funcione con las 4 operaciones básicas 
#(suma, resta, multiplicación y división). El programa ofrecerá un menú de 
#opciones al usuario para seleccionar la operación que desee realizar, pudiendo 
#realizar todas las operaciones que él desee, el número de veces que lo desee, 
#hasta que seleccione una opción para salir del programa.


#no terminado aun


lista=[]


def Suma():
    suma= 0
    cont= 1
    print("Has seleccionado SUMA!")
    cantop = (input(f"Cuántos números queres sumar?: "))
    if cantop.isnumeric() == True:
        for x in range(0,int(cantop)):
            num = (input(f"Ingresa el número {cont} a sumar: "))
            if num.isnumeric() == True:
                cont +=1
                suma += int(num)
                lista.append(num)
            else:
                print("Número no válido.")
            print(f"La suma total de los números es de: {suma}")
    else:
        print("Número no válido.") 
        Suma()

def Inicio():
    print("Calculadora super pro:")

    print("Opción a realizar: \n1 - Sumar \n2 - Restar\n3 - Multiplicar\n4 - Dividir")

    return input("Qué opción queres usar?").upper

Inicio()

    if return != "1" or opcion == "SUMAR":
        Suma()
    else:
        print("Opción no válida.") 
        Inicio()