# Escribe un programa donde tenaga una lista y que a continuacion,elimine loas elemento
#repetidos,por ultimo mostrar la lista
lista= [1,2,3,4,5,6,"Waldo",2,3,4]

conjunto = set(lista)

#lista = list(conjunto)
lista = list(set(lista))

print(lista)