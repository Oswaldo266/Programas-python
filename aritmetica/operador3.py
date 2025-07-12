def pedir_numeros():
    try:
        a = float(input("Ingrese un valor a -> "))
        b = float(input("Ingrese un valor b -> "))
        return a, b
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return None, None

print("Hacer un programa para intercambiar el valor de 2 variables")
print("Por ejemplo: si a = 10 y b = 5, después del cambio a = 5 y b = 10\n")

a, b = pedir_numeros()

if a is not None and b is not None:
    print(f"Valores originales: a = {a}, b = {b}")
    
    a, b = b, a
    
    print(f" Valores después del intercambio: a = {a}, b = {b}")
else:
    print("No se puede realizar el intercambio debido a un error en los datos.")
