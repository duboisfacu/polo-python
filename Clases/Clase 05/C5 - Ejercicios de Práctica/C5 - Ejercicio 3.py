#Realizar una funcipin donde el usuario ingrese cantidad de kilometros a recorrer, 
#la velocidad promedio de la ruta y cantidad de minutos de descanso que se tomará el conductor. 
#La misma debe devolver la cantidad de horas promedio que demorará en terminar el trayecto, 
#ese valor almacenarlo en una variable y mostrar un mensaje. 
#Ej: "Su tiempo de viaje será aproximadamente 20 horas"

def Calculo():
    km = int(input('Kilómetros a recorrer: '))
    vm = int(input('Velocidad promedio: '))
    descanso = int(input('Minutos de descanso: '))

    tiempo = km / vm + (descanso / 60)
    print("Su tiempo de viaje será aproximadamente", tiempo, "horas.")
    
Calculo()
