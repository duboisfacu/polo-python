#Vamos a simular el comportamiento de una
#API(*). Supongamos que conecto con un sistema para obtener el contenido
#de una base de datos de personas, y dicho sistema me los devuelve con el
#siguiente formato de string:

#"nombre;apellido;documento;sexo\nEzequiel;Etchecoin;12345678;M\nJoaquín;Mateos;87654321;M"

#Cada
#persona es separada utilizando el carácter de cambio de línea "\n", y
#el primer grupo indica los nombres de los datos en el orden en el que
#irán apareciendo en los siguientes grupos. Tomando el string del
#ejemplo, generar un diccionario que almacene las personas con sus datos,
#y los imprima por pantalla.

#(*) Application Programming
#Interface, interfaz de programación de aplicaciones, generalmente se
#trata de una de las capas externas a un sistema, que permite la
#comunicación con otros sistemas.

personas ={
    "nombre":["Ezequiel","Joaquín"],
    "apellido":["Etchecoin","Mateos"],
    "documento":["12345678","87654321"], 
    "sexo":["M","M"], 
}

for x in range((len(personas["nombre"]))):
    print(f'{personas["nombre"][x]};{personas["apellido"][x]};{personas["documento"][x]};{personas["sexo"][x]}')

