#Declarar 1 variable string que contenga cualquier texto 
#y mostrar en pantalla el texto repetido 10 veces. 
#Diseñar al menos 2 versiones que cumplan el mismo fin.

string1 = "Im not a robot"

#Versión 1
for x in range(10):
    print("Im not a robot")

#Versión 2
stop = 0

while True:
    if stop == 10:
        break
    else:
        print("Im not a robot")
    stop += 1