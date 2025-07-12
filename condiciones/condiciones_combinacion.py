def pedir_numero():
    try:

        Edad = int(input("Ingrese la edad: "))

        return Edad
    
    except ValueError:
        print("Ingreso un valor incorrecto")

        return None
print("Ingrese la edad para saber si ya es mayor de edad o menor de edad ")

Edad = pedir_numero()
if 0<Edad<120:
    print("Edad correcta")
    if Edad >= 18:
        print(f"Usted cumple para hacer mayor de edad: {Edad} anios")
else:
    print("Edad incorrecta")
