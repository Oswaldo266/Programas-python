#bucle while
import math

def pedir_numero():
    try:
        numero = int(input("Ingrese un numero: "))
        return numero
    except ValueError:
        print("no se ingreso un digito")
        return None
print("calcular la raiz cuadrada de un numero")

numero = pedir_numero()

while numero<0:
    print("Error--> deberia de ingresar un valor positivo")
    numero = int(input("Ingrese un numero: "))
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}:")
