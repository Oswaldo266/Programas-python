beatles = []# paso 1
print("Paso 1:", beatles)

# paso 2
beatles.append("john lennon")
beatles.append("paul McCartney")
beatles.append("George Harrison")

# paso 3
for i in range(2):
    a = input("Ingrese un sujeto de la banda a la lista: ")
    beatles.append(a)
    
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]

print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"ringo starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
