# CONTAR VOCALES DE UNA PALABRA

palabra = input("escribe una palabra: ").lower()
vocales = "aeiou"
contador_vocales = 0
i = 0

while i < len(palabra):
    if palabra[i] in vocales:
       contador_vocales += 1
    i += 1
print(f"La cantidad de vocales es: {contador_vocales}")

