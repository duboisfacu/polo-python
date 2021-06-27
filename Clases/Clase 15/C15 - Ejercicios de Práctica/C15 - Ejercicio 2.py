#Ejercicio de diccionario

diccionario = {
    "Name": "Elliot Alderson",
    "Born": "September 17, 1986",
    "Profession": "Cybersecurity Engineer",
    "Family": ["Magda", "Darlene", "Edward Alderson"]
}

def show():
    print("--------------------------------------------------------")
    print("1 - Name: ",diccionario["Name"])
    print("2 - Born: ",diccionario["Born"])
    print("3 - Profession: ",diccionario["Profession"])
    print("4 - Family: ",diccionario["Family"])
    print("--------------------------------------------------------")
show()

ListFamily =  diccionario["Family"]

while True:
    mod = input("Escribe el número a editar: ")
    if mod == "1":
        diccionario["Name"] = input("Ingresa el nuevo valor: ")
    elif mod == "2":
        diccionario["Born"] = input("Ingresa el nuevo valor: ")
    elif mod == "3": 
        diccionario["Profession"] = input("Ingresa el nuevo valor: ")
    elif mod == "4": 


        while True:
            print("--------------------------------------------------------")
            print("¿Qué deseas hacer con Family?")      
            print("1 - Borrar")
            print("2 - Modificar")
            print("3 - Agregar")
            print("4 - Volver")
            print("--------------------------------------------------------")
            mod = input("Escribe el número de la opción a realizar: ")
            if mod == "1":
                print("Familia actual: ",diccionario["Family"])
                print("Escribe exactamente el dato a borrar: ")
                textdel = input()

                if textdel in ListFamily:
                    indexdel = ListFamily.index(textdel)
                    list.pop(ListFamily,indexdel)
                    break
                else:
                    print(textdel,"no se encuentra en la lista.")
                    continue

            elif mod == "2":
                print("Familia actual: ",diccionario["Family"])
                print("Escribe exactamente el dato a modificar: ")
                textmod = input()
                
                if textmod in ListFamily:
                    indexmod = ListFamily.index(textmod)
                    textmod = input("Ingresa el nuevo valor: ")
                    ListFamily[indexmod] = textmod
                    break
                else:
                    print(textmod,"no se encuentra en la lista.")
                    continue    

            elif mod == "3":
                print("Familia actual: ",diccionario["Family"])
                print("Escribe el dato a agregar: ")
                textadd = input()
                ListFamily.append(textadd)
                break
            elif mod == "4":
                break
            else:
                print("Valor fuera de rango.")
                
    else:
        print("Valor fuera de rango.")

    show()

