def pedir_numeros():
    try:
        a_input = input("Ingrese el primer valor: ").strip()
        if a_input == "":
            raise ValueError("No ingresaste el primer número.")
        a = float(a_input)

        b_input = input("Ingrese el segundo valor: ").strip()
        if b_input == "":
            raise ValueError("No ingresaste el segundo número.")
        b = float(b_input)

        return a, b
    except ValueError as e:
        print(f"Error: {e}")
        return None, None


historial = []

while True:
    opcion = input(
        "Ingresa una opción: \nS. Suma\nR. Resta\nM. Multiplicación\nD. División\n%. Módulo\n0. Salir\n"
    ).upper()

    opciones_validas = {"S", "R", "M", "D", "%", "0"}
    if opcion not in opciones_validas:
        print("Opción inválida. Intenta de nuevo.\n")
        continue

    if opcion == "0":
        print("\nSaliste del programa.")
        break

    a, b = pedir_numeros()
    if a is None or b is None:
        continue

    if opcion == "S":
        resultado = a + b
        operacion = f"Suma: {a} + {b} = {resultado}"
    elif opcion == "R":
        resultado = a - b
        operacion = f"Resta: {a} - {b} = {resultado}"
    elif opcion == "M":
        resultado = a * b
        operacion = f"Multiplicación: {a} * {b} = {resultado}"
    elif opcion == "D":
        if b == 0:
            print("No se puede dividir entre cero.\n")
            continue
        resultado = a / b
        operacion = f"División: {a} / {b} = {resultado}"
    elif opcion == "%":
        if b == 0:
            print("No se puede usar módulo con cero.\n")
            continue
        resultado = a % b
        operacion = f"Módulo: {a} % {b} = {resultado}"
    else:
        print("Opción no válida. Intenta de nuevo\n")
        continue

    print(f"El resultado es: {resultado}\n")
    historial.append(operacion)

    volver = input("¿Deseas hacer otra operación? (s/n): ").strip().lower()
    if volver != "s":
        print("\nGracias por usar la calculadora. ¡Hasta luego!\n")
        break

# Guardar historial en archivo de texto
if historial:
    with open("historial_operaciones.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Historial de operaciones realizadas:\n")
        for i, oper in enumerate(historial, 1):
            archivo.write(f"{i}. {oper}\n")
    print("El historial se guardó en 'historial_operaciones.txt'.")
else:
    print("No realizaste ninguna operación.")
