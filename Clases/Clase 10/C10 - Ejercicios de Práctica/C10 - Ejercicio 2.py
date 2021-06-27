#Escribir un programa que pida al usuario su ingreso mensual, 
#pregunte si está en relación de dependencia y calcule cuanto 
#será su ingreso total entre Enero y Diciembre, incluyendo 
#aguinaldo en caso de que corresponda


ingreso=int(input("¿Cuál es su ingreso mensual?: "))
dependencia=input("¿Se encuentra en relación de dependencia? (SI/NO): ")
aguinaldo = ingreso * 0.50

if dependencia.lower() == "si":
    print("Su pago va a ser de $", ingreso * 12 + aguinaldo)
elif dependencia.lower() == "no":
    print("Su pago va a ser de $", ingreso * 12)
else:
    print("Seguro que puso 'SI o 'NO'?")
