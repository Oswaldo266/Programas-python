def pedir_numero():
    try:
        precio = float(input("Ingrese el valor de la compra: "))
        return precio
    except ValueError:
        print("Ingrese un valor positivo")
        return None

print("Una tienda ofrece un desscuento del 15% sobre un total de la compra")
print("y un cliente desea saber cuanto debera de pagar finamente por su compra.")

precio = pedir_numero()

if a is not None:
    descuento= precio * 0.15
    resultado = precio - descuento
    print(f"El descuento es de : {descuento: .2f}$")
    print(f"Su compra total con descuento es de: {resultado: .2f}$")
else:
    print("Error al aplicar el descuento")
