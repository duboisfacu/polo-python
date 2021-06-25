#Realizar un programa que calcule el IMC (Indice de masa corporal), 
#utilizando la interacción con el usuario pidiendo el peso y la altura. 
#Utilizar una función reciba estos datos por parámetro, haga el 
#calculo y muestre el resultado
#FORMULA: IMC = pesoEnKilogramos / (alturaEnMetros * alturaEnMetros))

peso = int(input('¿Cuál es tu peso?\n'))
altura = float(input('¿Cuál es tu altura? (ej: 1.67)\n'))

def calculo():
    IMC= peso / (altura * altura)
    print(IMC)

calculo()
