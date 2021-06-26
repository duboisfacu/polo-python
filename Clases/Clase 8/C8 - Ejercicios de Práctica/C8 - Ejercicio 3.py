#Crear un programa que determine el precio de venta de lapiceras. 
#*El programa debe solicitar el precio unitario y la cantidad. 
#*Si la cantidad supera las 100 unidades, se debe realizar un descuento del 15%.
#*Mostrar Subtotal - Total - Total Descuento

precio = int(input('¿Cuánto vale cada lapicera?: '))
cantidad = int(input('¿Cuántas lapiceras va a comprar?: '))

if cantidad > 100:
    print("Le va a costar", cantidad * precio - cantidad * precio * 0.15 ,"pesos.")
else:
    print("Le va a costar", cantidad * precio,"pesos.")