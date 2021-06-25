#Realizar un programa que pregunte al usuario en que 
#numero de mes estamos (Mayo = 5) y calcule 
#cuantos meses faltan para terminar el año

mes = input('¿En qué mes estamos?\n')
restantes= 12 - int(mes)
print("Faltan:", restantes, "meses para terminar el año.")