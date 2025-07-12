from sympy import symbols, integrate

x = symbols('x')
f = x**2 + 2*x + 1

resultado = integrate(f, x)
print("Resultado de la integral:", resultado)
