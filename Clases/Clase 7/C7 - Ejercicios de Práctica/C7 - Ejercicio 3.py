#Solicitar el ingreso de la cantidad de días que ya pasaron del año, 
#luego llamar una función que ejecute una evaluación para saber 
#si ya pasamos o no la mitad del año. Dicha función debe retornar 
#un True o un False según el caso y luego imprimir según ese 
#valor un mensaje. En caso de True el mensaje es "ya estamos en 
#la segunda mitad del año", en caso de Flase 
#"todavía estamos en la primer mitad del año"

transcurso = int(input('¿Cuántos días van del año?: '))

def Evaluación():
    if transcurso > (365/2):
        return True
    else:
        return False

Evaluación()

if Evaluación() == True:
    print("ya estamos en la segunda mitad del año")
elif Evaluación() == False:
    print("todavía estamos en la primer mitad del año")

print("sexo")