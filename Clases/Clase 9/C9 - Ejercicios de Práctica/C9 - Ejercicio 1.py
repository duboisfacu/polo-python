#1) Dados 3 números que ingrese el usuario, mostrar por pantalla los siguientes resultados condicionalmente:
#        a) Si el 3ro es el mayor de los números, mostrar la sumatoria de los 3
#        b) Si el 1ro es el mayor, mostrar el producto (multiplicación) de los 3
#        c) Si los 3 números son iguales, hacer que el usuario ingrese un 4to número e imprimir la resta entre ellos, de manera secuencial (1 - 2 - 3 - 4)
#Procurar extraer cada operación y texto en pantalla en una función (una para la suma, una para la multiplicación, etc).

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

def Suma():
    print(num1 + num2 + num3)

def Resta():
    num4 = int(input('Ingrese el cuarto número: '))
    print(num1 - num2 - num3 - num4)

def Multiplicacion():
    print(num1 * num2 * num3)

if num3 > num1 and num3 > num2:
    Suma()
elif num1 > num2 and num1 > num3:  
    Multiplicacion()
elif num1 == num2 and num2 == num3:  
    Resta()
