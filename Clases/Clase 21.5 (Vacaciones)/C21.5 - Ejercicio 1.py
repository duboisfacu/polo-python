# Diseñar un programa que calcule el máximo común divisor (MCD) entre
# dos números. El máximo común divisor entre dos números se define como el
# mayor número que puede dividir a ambos candidatos, con resto 0
# (división exacta).

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

cont = 0
mayor = 0
while True:
    cont += 1
    if num1 % cont == 0 and num1 % cont == 0:
        mayor = cont

    if cont > num1 and cont > num2:
        break

print(f'si {mayor}')