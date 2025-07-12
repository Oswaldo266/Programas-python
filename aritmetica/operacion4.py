import math

def pedir_numeros():
    try:
        r= float(input("Ingrese el valor de la radio: "))
        return r 
    except ValueError:
        print("Error: ingrese un valor valido")
def redondear(valor, decimales=2):
    return round(valor, decimales)



print("Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longityud de la circuferencia ")

r= pedir_numeros()

if r is not None:
    area= math.pi * r**2
    Longitud= 2 * math.pi * r


    
    area = redondear(area, 2)
    longitud = redondear(Longitud, 2)


    print(f"El area es de: {area}")
    print(f"La longitud es: {longitud}")
else:
    print("No salio xd")