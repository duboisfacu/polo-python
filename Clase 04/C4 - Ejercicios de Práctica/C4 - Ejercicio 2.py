#Realizar un programa que pida el nombre de una persona, 
#luego pida el apellido y por ultimo pida el año de nacimiento. 
#Pasar estos datos a una función la cual calcule la edad de la 
#persona y lo salude de la siguiente manera: "Hola Juan Perez, 
#según nuestros cálculos, usted tiene 32 años"

nombre = input('¿Cuál es tu nombre?\n')
apellido = input('¿Cuál es tu apellido?\n')
anio = input('¿Cuál es tu año de nacimiento?\n')

def calculo():
    edad = 2021 - int(anio)
    print("Hola", nombre, apellido + ", según nuestros cálculos, usted tiene", edad , "años")

calculo()