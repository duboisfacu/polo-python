#Vamos a crear un conversor de temperatura entre grados centígrados (C) 
#y grados Fahrenheit (F). Solicitaremos al usuario que ingrese la 
#temperatura y en qué medida se encuentra, e imprimiremos en pantalla 
#la temperatura convertida. Utilizar las siguientes fórmulas para la conversión:

#de C° a F° => (°C * 9/5) + 32
#de F° a C° => (°F - 32) * 5/9

temp = int(input("Ingrese la temperatura a convertir: "))
medida = (input("Ingese la medida en la que se encuentra (F=F° - C = C°): "))

if medida == "C" or medida == "c":
    print(str(temp) + " grados centígrados equivalen a " + str((temp * 9/5) + 32) + "F°")

elif medida == "F" or medida == "f":
    print(str(temp) + " grados Fahrenheit equivalen a " + str((temp - 32) * 5/9) + "C°")

else:
    print("Medida incorrecta.")