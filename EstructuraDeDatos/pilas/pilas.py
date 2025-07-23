#pilas

pila=[1,2,3]
#agrgando elementos al final
pila.append(4)
pila.append(5)
print(pila)
#sacando elementos por el final
n = pila.pop()#retorna el valor
print(f"sacando el elemento {n}")
n = pila.pop()
print(f"sacando el elemento {n}")

print(pila)