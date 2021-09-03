#readlines recorre lineas
with open("Clases/Clase 23/C23 - Ejercicios de práctica/C23 - Archivo 1.txt","r") as archivo:
    renglones = archivo.readlines()
    for renglon in renglones:
        print(renglon)
