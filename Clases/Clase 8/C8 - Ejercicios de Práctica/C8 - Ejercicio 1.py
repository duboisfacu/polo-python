#Crear un programa que solicite nombre y apellido
#*Si el nombre completo supera los 15 caracteres, 
#mostrar un mensaje en pantalla al usuario diciendo que 
#tiene un nombre muy largo. Sino, que es muy corto.

nombre = (input('Ingrese su nombre: '))
apellido = (input('Ingrese su apellido: '))
nombrecompleto= nombre + apellido

if len(nombrecompleto) > 15:
    print("Tiene un nombre muy largo.")
else:  
    print("Tiene un nombre muy corto.")