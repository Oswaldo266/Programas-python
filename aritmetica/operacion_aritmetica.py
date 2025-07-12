def pedir_numeros():
    try:
        a = float(input("ingrese un valor a-> "))
        b = float(input("ingrese un valor b-> "))
        c = float(input("ingrese un valor c-> "))
        return a,b,c 
    except ValueError:
        print("Erro: Ingrese valores numericos validos.")
        return None, None, None
 
print("Bienvenidos a la solucion de la Ec (a^3 * (b^2 - 2ac)/(2b) \n")

a, b, c = pedir_numeros()


if b==0:
        print("Error: b no puede ser cero " )
else:
        resultado = (a**3 * (b*2 - 2*a*c))/(2*b)
        print("Resultado de la operacion es de: ", resultado )

