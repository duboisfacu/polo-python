#Realizar una función donde solicite al usuario ingresar 
#cantidad de horas trabajadas por día, 
#cantidad de días trabajados en el mes 
#y el precio por hora. Y que devuelva el sueldo a cobrar, 
#almacenar ese valor en una variable y luego imprimirlo por consola.

def Calculo():
    horas = int(input('Horas trabajadas por día: '))
    dias = int(input('Días trabajados al mes: '))
    precio = int(input('Precio por hora: '))
    sueldo = precio * horas * dias
    print("Tu sueldo a cobrar es de", sueldo, "pesos.")
    
Calculo()
