print("-------Bienvenidos a la calculado de Division----")

try:
    A= float(input("Ingrese el valor de a: "))
    B= float(input("Ingrese el valor de b: "))

    resultado= A/B
    print(f"El resultado de la division {resultado}")
    
except ValueError:
    print("Error: Ingrese los valores validos")