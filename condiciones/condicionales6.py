def pedir_numeros():
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        c = float (input("Ingrese el tercer numero: "))
        return a, b, c
    except ValueError:
        print("VALORES INCORRECTOS")
        return None, None, None
print("Hacer un programa que pida 3 numeros y determine cual es mayor a>b>c")

a,b,c= pedir_numeros()

if a is not None and b is not None and c is not None:
    if a >= b and a>=c:
        print(f"El numero mayor es: {a} ")
    elif b>=a and b>=c:
        print(f"El numero mayor es: {b}")
    elif c>=a and c>=b:
        print(f"El numero mayo es {c}")
else:
    print("fin")
 