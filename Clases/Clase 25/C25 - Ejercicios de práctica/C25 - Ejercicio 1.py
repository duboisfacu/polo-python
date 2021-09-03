import json

with open("Clases/Clase 25/C25 - Ejercicios de práctica/C25 - Archivo.json","r") as archivo:
    diccionarioJSON = dict(json.load(archivo))
    for clave, valor in diccionarioJSON.items():
        print(clave + ":", valor)