#Crear una calculadora básica que funcione con las 4 operaciones básicas 
#(suma, resta, multiplicación y división). El programa ofrecerá un menú de 
#opciones al usuario para seleccionar la operación que desee realizar, pudiendo 
#realizar todas las operaciones que él desee, el número de veces que lo desee, 
#hasta que seleccione una opción para salir del programa.




lista=[]
opcion= None

def Suma():
    suma= 0
    cont= 1
    print("-------------------------------------------")
    print("Has seleccionado SUMA!")
    print("-------------------------------------------")
    cantop = (input(f"Cuántos números queres sumar?: "))
    if cantop == "1":
        print("-------------------------------------------")
        print("Se suma de a 2 números crack.")
        print("-------------------------------------------")
    elif cantop.isnumeric() == True:
        for x in range(0,int(cantop)):
            num = (input(f"Ingresa el número {cont} a sumar: "))
            if num.isnumeric() == True:
                cont +=1
                suma += int(num)
                lista.append(num)
            else:
                print("-------------------------------------------")
                print("Número no válido.")
                print("-------------------------------------------")
                break
        print("-------------------------------------------")
        print(f"La suma total de los números es de: {suma}")
        print("-------------------------------------------")
    else:
        print("Número no válido.")
        print("-------------------------------------------")
        Inicio()

def Resta():
    lista.clear()
    resta= 0
    cont= 1
    print("-------------------------------------------")
    print("Has seleccionado RESTA!")
    print("-------------------------------------------")
    cantop = (input(f"Cuántos números queres restar?: "))
    if cantop == "1":
        print("-------------------------------------------")
        print("Se resta de a 2 números crack.")
        print("-------------------------------------------")
    elif cantop.isnumeric() == True:
        for x in range(0,int(cantop)):
            num = (input(f"Ingresa el número {cont} a restar: "))
            if num.isnumeric() == True:
                cont +=1
                if len(lista) == 0:
                    resta = int(num)
                    lista.append(num)
                else:
                    resta = resta - int(num)
                    lista.append(num)    
            else:
                print("-------------------------------------------")
                print("Número no válido.")
                print("-------------------------------------------")
                break
        print("-------------------------------------------")
        print(f"La resta total de los números es de: {resta}")
        print("-------------------------------------------")
    else:
        print("Número no válido.")
        print("-------------------------------------------")
        Inicio()

def Multiplicacion():
    lista.clear()
    multiplicacion= 0
    cont= 1
    print("-------------------------------------------")
    print("Has seleccionado MULTIPLICACIÓN!")
    print("-------------------------------------------")
    cantop = (input(f"Cuántos números queres multiplicar?: "))
    if cantop == "1":
        print("-------------------------------------------")
        print("Se multiplica de a 2 números crack.")
        print("-------------------------------------------")
    elif cantop.isnumeric() == True:
        for x in range(0,int(cantop)):
            num = (input(f"Ingresa el número {cont} a multiplicar: "))
            if num.isnumeric() == True:
                cont +=1
                if len(lista) == 0:
                    multiplicacion = int(num)
                    lista.append(num)
                else:
                    multiplicacion = multiplicacion * int(num)
                    lista.append(num)    
            else:
                print("-------------------------------------------")
                print("Número no válido.")
                print("-------------------------------------------")
                break
        print("-------------------------------------------")
        print(f"La multiplicación total de los números es de: {multiplicacion}")
        print("-------------------------------------------")
    else:
        print("Número no válido.")
        print("-------------------------------------------")
        Inicio()

def Division():
    lista.clear()
    division= 0
    cont= 1
    print("-------------------------------------------")
    print("Has seleccionado DIVISIÓN!")
    print("-------------------------------------------")
    cantop = (input(f"Cuántos números queres dividir?: "))
    if cantop == "1":
        print("-------------------------------------------")
        print("Se divide de a 2 números crack.")
        print("-------------------------------------------")
    elif cantop.isnumeric() == True:
        for x in range(0,int(cantop)):
            num = (input(f"Ingresa el número {cont} a dividir: "))
            if num.isnumeric() == True:
                cont +=1
                if len(lista) == 0:
                    division = int(num)
                    lista.append(num)
                else:
                    division = division / int(num)
                    lista.append(num)    
            else:
                print("-------------------------------------------")
                print("Número no válido.")
                print("-------------------------------------------")
                break
        print("-------------------------------------------")
        print(f"La división total de los números es de: {division}")
        print("-------------------------------------------")
    else:
        print("Número no válido.")
        print("-------------------------------------------")
        Inicio()







def Inicio():
    
    print("Calculadora super pro:")
    print("-------------------------------------------")
    opcion = input("Opción a realizar: \n1 - Sumar \n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Salir\n")

    if opcion == "1" or opcion == "SUMAR":
        Suma()
        Inicio()
    elif opcion == "2" or opcion == "RESTAR":
        Resta()
        Inicio()
    elif opcion == "3" or opcion == "MULTIPLICAR":
        Multiplicacion()
        Inicio()
    elif opcion == "4" or opcion == "DIVIDIR":
        Division()
        Inicio()
    elif opcion == "5" or opcion == "SALIR":
        exit()
    else:
        print("Opción no válida.") 
        Inicio()

Inicio()


