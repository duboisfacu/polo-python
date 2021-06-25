#Diseñar una app que actúe como un cajero. El usuario ingresará un monto de dinero que desea retirar (número entero) 
#y deberemos indicarle la cantidad de billetes y/o monedas de cada denominación que le ofreceremos, 
#suponiendo que los billetes y monedas no se nos acaban. Por ejemplo:
#Usuario ingresa: 4.565
#Mostraremos por pantalla:
#        4 billetes de 1000
#        1 billete de 500
#        1 billete de 50
#        1 billete de 10
#        1 moneda de 5

monto = int(input('¿Cuánto desea retirar?: '))

if monto / 1000 > 0:
    billetes = int(monto / 1000)
    if billetes > 0:
        print(billetes, "billetes de 1000")
        monto= monto - billetes * 1000

if monto / 500 > 0:
    billetes = int(monto / 500)
    if billetes > 0:
        print(billetes, "billetes de 500")
        monto= monto - billetes * 500

if monto / 50 > 0:
    billetes = int(monto / 50)
    if billetes > 0:
        print(billetes, "billetes de 50")
        monto= monto - billetes * 50

if monto / 10 > 0:
    billetes = int(monto / 10)
    if billetes > 0:
        print(billetes, "billetes de 10")
        monto= monto - billetes * 10

if monto / 5 > 0:
    billetes = int(monto / 5)
    if billetes > 0:
        print(billetes, "billetes de 5")
        monto= monto - billetes * 5