print("-------Bienvenidos a la Calculadora ------")

while True:
    opcion = int(input("Ingresa una opción: \n 1.suma\n 2.resta\n 3.Multiplicacion\n 4.division\n 5.modulo\n 0 para salir \n"))
    
    match opcion:
        case 1:
            print("Elegiste 1\n")
            print("Bienvenido a la suma uwu ")
            try:
                A= float(input("Ingrese el valor de a: "))
                B= float(input("Ingrese el valor de b: "))

                resultado= A+B
                print(f"El resultado de la suma es {resultado}")
    
            except ValueError:
                print("Error: Ingrese los valores validos")
       
       
        case 2:
            print("Elegiste 2")
            print("-------Bienvenidos a la resta----")

            try:
                  A= float(input("Ingrese el valor de a: "))
                  B= float(input("Ingrese el valor de b: "))

                  resultado= A-B
                  print(f"El resultado de la resta es {resultado}")
    
            except ValueError:
             print("Error: Ingrese los valores validos")
       
       
       
        case 3:
            print("Elegiste 3")
            print("-------Bienvenidos a la Multiplicacion----")

            try:
                A= float(input("Ingrese el valor de a: "))
                B= float(input("Ingrese el valor de b: "))

                resultado= A*B
                print(f"El resultado de la Multiplicacion {resultado}")
    
            except ValueError:
              print("Error: Ingrese los valores validos")
       
       
        case 4:
            print("Elegiste 4")
            print("-------Bienvenidos a la Division----")

            try:
                A= float(input("Ingrese el valor de a: "))
                B= float(input("Ingrese el valor de b: "))

                resultado= A/B
                print(f"El resultado de la division {resultado}")
    
            except ValueError:
                print("Error: Ingrese los valores validos")
      
      
        case 5:
            print("Elegiste 5")
            print("------- Bienvenidos a al Modulo ----")

            try:
                A= float(input("Ingrese el valor de a: "))
                B= float(input("Ingrese el valor de b: "))

                resultado= A%B
                print(f"El resultado de la modulo {resultado}\n")
    
            except ValueError:
             print("Error: Ingrese los valores validos")


        case 0:
            print("Saliendo del programa...")
            break  
        case _:
            print("Opción no válida")

