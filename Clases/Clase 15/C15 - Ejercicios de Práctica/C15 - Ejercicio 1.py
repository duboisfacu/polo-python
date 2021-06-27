#Ejercicio de tuplas

listameterias=[]

alumno = input("Agregar alumno: ")

print("Alumno cargado correctamente.")

print("Para dejar de cargar materias escribe '0'")

while True:
    meteria = (input("Agregar materia: "))
    if meteria == "0":
        break
    else:
        listameterias.append(meteria)
        continue

print("-----------------------------------------")
def obtenerDatos():
    return (alumno, listameterias)

registroDeBaseDatos = obtenerDatos()

nombreAlumno, asignaturasList = registroDeBaseDatos
print("El alumno: ",nombreAlumno)
print("Esta anotado en las materias: ", asignaturasList)