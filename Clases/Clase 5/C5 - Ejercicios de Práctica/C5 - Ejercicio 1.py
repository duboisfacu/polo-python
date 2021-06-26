#Realizar una función que solicite al usuario que ingrese:
#-Total de Gastos
#-Total de Ventas
#Y que imprima en pantalla:
#-Ganancia
#-% de rentabilidad 


gastos = int(input('Total de Gastos:'))
ventas = int(input('Total de Ventas:'))

def Calculo():
    ganancia = ventas - gastos
    rentabilidad = ganancia / gastos
    print("La ganancia fue de", ganancia, "pesos.")
    print("La rentabilidad fue del", rentabilidad, "%.")
    
Calculo()
