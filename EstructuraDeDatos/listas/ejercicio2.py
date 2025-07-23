#escriba un programa que tenga dos lista y que, a continuacion, cree las siguienteslista
#(en las que no debe de haber repeticiones)
#1.lista de elementos que aparecen en las dos lista
#2.lista de elementos que aparecen en la primera lista,pero no en la segunda
#3. lista de elementosque aparecen en la segunda lsita,peero no aparescan en la primera
#4.lista de elementosque aparecen en ambas listas

lista1= [1,2,3,4,5,6,4,3,2,1,5,6]
lista2 = [4,5,6,7,8,9,1,2,3,4,5,]
#eliminar repetidos ambas lista
a = set(lista1)
b = set(lista2)

union = list(a|b)
soloA = list(a-b)
soloB = list(b-a)
interseccion = list(a & b)

print(f"#1.lista de elementos que aparecen en las dos lista {union}")
print(f"#2.lista de elementos que aparecen en la primera lista,pero no en la segunda {soloA}")
print(f"#3. lista de elementosque aparecen en la segunda lsita,peero no aparescan en la primera {soloB}")
print(f"#4.lista de elementosque aparecen en ambas listas {interseccion}")