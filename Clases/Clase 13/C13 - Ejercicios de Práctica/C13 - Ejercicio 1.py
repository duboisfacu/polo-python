#Hacer que el usuario ingrese un texto, y mostrar por pantalla 
#si se trata de un palíndromo 
#(frase o palabra que se lee igual al derecho y al revés). 

#Ejemplos que tienen que informar como veraderos:
#"neuquen" 
#"Neuquen" 
#"menem"
#"meNem"
#"anana"
#"12321"
#"1234.321"

#"No subas abuson"
#"No subas, abuson"


while True:
    texto= input("Ingresa un texto:")
    textolistado = list(texto)
    textolistado.reverse()
    textolistado = str.join("", textolistado)

    if texto == textolistado:
        print("El texto que ingresaste es un palíndromo!")
        break
    else:
        continue
