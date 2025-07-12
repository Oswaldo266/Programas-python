print("-------Bienvenidos a la calculado de Multiplicacion----")

try:
    A= float(input("Ingrese el valor de a: "))
    B= float(input("Ingrese el valor de b: "))

    resultado= A*B
    print(f"El resultado de la Multiplicacion {resultado}")
    
except ValueError:
    print("Error: Ingrese los valores validos")