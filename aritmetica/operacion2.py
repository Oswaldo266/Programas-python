def pedir_numeros():
    try:
        a = float(input("Ingrese un valor a -> "))
        b = float(input("Ingrese un valor b -> "))
        c = float(input("Ingrese un valor c -> "))
        d = float(input("Ingrese un valor d -> "))
        e = float(input("Ingrese un valor e -> "))
        f = float(input("Ingrese un valor f -> "))
        return a, b, c, d, e, f  
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return None, None, None, None, None, None

print("Bienvenido a la solución de la expresión lógica:")
print("((a + b * c) < d and ((-6 / 3 * 4) + 2 < 2)) or (e > f)\n")

a, b, c, d, e, f = pedir_numeros()

# Verificamos que no haya valores faltantes
if None in (a, b, c, d, e, f):
    print("No se puede continuar por datos inválidos.")
elif b == 0:
    print(" Error: No se puede dividir sobre 0.")
else:
    resultado = ((a + b * c) < d and ((-6 / 3 * 4) + 2 < 2)) or (e > f)
    print(f"El resultado de la operación es: {resultado}")
