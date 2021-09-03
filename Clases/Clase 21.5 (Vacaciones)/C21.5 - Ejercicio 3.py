#Diseñar un programa que pida al usuario ingresar un texto cualquiera, y
#cuente las ocurrencias de cada palabra del texto. Por ejemplo, el
#usuario ingresa "la casa de mi amigo Javier queda cerca de la casa de mi mamá", la salida debería ser la siguiente:
#"la": 2,
#"casa": 2,
#"de": 2,
#"mi": 2,
#"amigo": 1,
#"Javier": 1,
#...


frase = (input("Ingrese una frase: ")).split()
cont = 0
palabra = ""
for n in frase:
    palabra = n
    for pal in frase:
        if palabra == pal:
            cont +=1
    print(palabra, cont)   
    cont = 0

