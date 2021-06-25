#Solicitar el ingreso de dos números al usuario, 
#y luego de obtenerlos imprimir el siguiente mensaje 
#"El primer número es mayor o igual al segundo" o 
#"El primer número es menor al segundo"

num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))

if num1 >= num2:
    print("El primer número es mayor o igual al segundo")
else:  
    print("El primer número es menor al segundo")

