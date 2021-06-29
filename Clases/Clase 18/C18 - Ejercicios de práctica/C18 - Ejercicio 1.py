#1) Crear un programa que solicite al usuario 
#un conjunto de números, y muestre el promedio entre todos ellos.

numeros=[]

print("Ingrese numeros para promediar, salga con la palabra 'SALIR': ")

cont = 0
total = 0
while True:
    num = input(f"Ingrese el número {cont + 1}: ").strip().upper()
    if num == "SALIR":
        break
    if num.isnumeric() == True:
        cont += 1 
        total+= int(num)
        numeros.append(num)
    else:
        print("Número no válido.")
        continue
    
print(numeros)
print(f"La cantidad de números cargados es de {cont}.")
print(f"La suma del total de números cargados es de {total}.")
print(f"El promedio es de {total/cont}.")