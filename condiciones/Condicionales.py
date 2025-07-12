# condiciones

def pedir_numero():
    try:
        numero = int(input("Ingrese un número: "))
        return numero
    except ValueError:
        print("No ingresó un número válido (quizá una letra o símbolo no permitido).")
        return None

numero = pedir_numero()

if numero is not None:
    print("Comprobando si el número ingresado es positivo, negativo o cero...")

    if numero > 0:
        print("El número es positivo\n")
    elif numero < 0:
        print("El número es negativo\n")
    else:
        print("El número es cero\n")
else:
    print("No se pudo evaluar el número porque no fue ingresado correctamente.\n")
