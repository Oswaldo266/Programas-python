#cajero automatico
def pedir_dinero(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("No se agregó una cantidad válida.")
        return 0.0
historial= []


saldo= 1000
print(f"Saldo inicial es de {saldo}")
while True:
    opcion = input(
        "-------------------menu------------------\n"
        "1. Ingresar dinero\n"
        "2. Retirar dinero\n"
        "3. Mostrar saldo disponible\n"
        "4. Salir\n"
        "Elige una opción (1-4): "
    ).upper()
    opcion_validas= {"1", "2","3","4"}
    if opcion not in opcion_validas:
        print("Opción inválida. Intenta de nuevo.\n")
        continue
    if opcion == "4":
        print("has salido del cajero")
        break
    
    elif opcion =="1":
        print("---------------Bienvenido----------- ")
        monto= pedir_dinero("Ingrese la cantidad que va a depositar ")
        saldo+=monto
        print(f"La cantidad que ingreso es de: {monto} ")
        print(f"Saldo actualizado {saldo}\n")
        continue
    elif opcion =="2":
        print("---------------Bienvenido----------- ")
        monto=pedir_dinero("Ingrese cantidad a retirar: ")
        if monto> saldo:
            print("saldo insuficiente")
        else:
            saldo-=monto
            print(f"Has ingresado: {monto}")
            print(f"Saldo actualizado {saldo}\n")
        continue
    elif opcion=="3":
        print(f"Saldo disponiblees : {saldo}")
        
    else:
        print("Error")
