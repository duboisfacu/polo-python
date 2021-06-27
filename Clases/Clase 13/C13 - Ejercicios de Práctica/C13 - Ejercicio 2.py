#Escribir un programa de rifas para el cual tendremos que 
#pedir 5 premios y su numero ganador, ejemplo: Premio: Asado - Numero: 27

#Luego preguntar al usuario cual es el numero de rifa 
#que compró y mostrar un mensaje tanto si tiene premio o 
#si debe seguir participando.

premios= []
numeros= []

for x in range(2):
    premios.append(input("Ingrese el premio:"))
    numeros.append(input("Ingrese el numero:"))

import os
os.system("cls")

print("La lista de premios es:", premios)

while True:
    print("No ingreses un valor para salir.")
    rifa=input("¿Cuál es tu número de rifa?: ")

    if len(rifa) < 1:
        print("Gracias por participar.")
        break

    if rifa in numeros:
        valor = numeros.index(rifa)
        print("Ganaste! Tu premio es:", premios[valor])
        break
    else:
        print("Perdiste, seguí participando!")
        continue
    
    