def obtener_vocales(texto):
    try:
        vocales = "aeiouAEIOU"
        return [letra for letra in texto if letra in vocales]
    except ValueError:
        print("No se ingresó palabra o frase.")
        return []

def obtener_no_vocales(texto):
    try:
        vocales = "aeiouAEIOU"
        return [letra for letra in texto if letra not in vocales and letra.isalpha()]
    except ValueError:
        print("No se ingresaron vocales.")
        return []

# Programa principal
texto = input("Ingrese una palabra o frase: ")

solo_vocales = obtener_vocales(texto)
solo_no_vocales = obtener_no_vocales(texto)

print(f"Vocales encontradas: {solo_vocales}")
print(f"No vocales encontradas: {solo_no_vocales}")
