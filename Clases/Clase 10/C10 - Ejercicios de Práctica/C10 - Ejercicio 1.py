#Escribí una función que, dada una cadena de texto, 
#limpie los espacios en blanco al inicio y al final, 
#luego debe mostrar un mensaje diciendo si la cantidad 
#de caracteres en la cadena es un número par o impar. 
#Pedir 3 nombres al usuario y llamar a esta función cada vez

def limpiar():
    cadena.strip()
    if len(cadena) % 2 == 0:
        print("La cantidad de carácteres en la cadena es un número par.")
    else:
        print("La cantidad de carácteres en la cadena es un número impar.")


for x in range(3):
    cadena = input("Ingrese el nombre a convertir:")
    limpiar()
