#Hacer que el usuario ingrese 2 textos por separado (en 2 inputs). Pueden ser números, símbolos, letras, lo que quiera.
#Si ingresa 2 números, mostrar la división entre ellos.
#Si ingresa 1 número y un texto, comunicar al usuario que el texto será su nombre de usuario y el número su PIN (número de identificación personal).
#Si ingresa 2 textos, retirar todos los espacios e imprimir ambos textos unidos en pantalla, contando la cantidad de caracteres que posee.

valor1 = (input('Primer texto: '))
valor2 = (input('Segundo texto: '))

numero1 = valor1.isnumeric()
numero2 = valor2.isnumeric()

if (numero1) and (numero2):
    print(numero1/numero2)
elif not (numero1) and not(numero2):
    print(valor1.strip() + valor2.strip(), "tiene un total de",len(valor1.strip() + valor2.strip()),"carácteres.")
else:
    if (numero1):
        print("Su nombre será:", valor2, "y su PIN será:", valor1)
    else:
        print("Su nombre será:", valor1, "y su PIN será:", valor2)

    