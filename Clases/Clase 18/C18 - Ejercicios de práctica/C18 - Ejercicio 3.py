#hacer que el usuario ingrese palabras o textos
#hasta ingresar un espacio en blanco o un texto vacio

while True:
    inp=input("Ingrese un texto: ").strip()
    if len(inp) < 1:
        break
print("Saliste!")