#Escribir un programa que pida al usuario dos palabras, 
# y que indique cuál de ellas es la más larga 
# y por cuántas letras lo es. Debe comprobar si 
# tienen la misma longitud y mostrar un mensaje en 
# ese caso, y si el usuario ingresa un texto vacío o 
# solo espacios en blanco no se debe hacer ninguna 
# comparación y directamente informar que debe ingresar textos válidos.

p1 = str(input("Ingrese una palabra: ")).strip()
p2 = str(input("Ingrese otra palabra: ")).strip()

if len(p1) == 0 or len(p2) == 0:
    print("Por favor ingresá textos válidos.")
elif len(p1) == len(p2):
    print("Ambas palabras tienen la misma longitud.")
elif len(p1) > len(p2):
    diferencia= len(p1) - len(p2)
    print(p1, "es más larga que", p2 ,"por", diferencia,"letras.")
else:
    diferencia= len(p2) - len(p1)
    print(p2, "es más larga que", p1 ,"por", diferencia,"letras.")