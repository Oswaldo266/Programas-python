def pedir_numeros():
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        return a , b
    except ValueError:
        print("No ingreso numero o un simbolo no aceptado")
        return None , None
print("Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son")

a,b = pedir_numeros()

if a%2==0 and b % 2 == 0:
    print(f"ambos numeros son pares {a} y {b}")
elif a%2==0 and b % 2!=0:
    print(f"{a} es par pero  {b} no es par")
elif a%2!=0 and b % 2==0:
    print(f"{a} es inpar pero  {b} es par")
elif a%2!=0 and b%2!=0:
    print(f"{a} y {b} no son pares")
else:
    print("Fin del programa")
