# =========================================================
# CONSIGNA: Pedile al usuario una palabra y contá cuántas
# vocales y cuántas consonantes tiene, usando un único
# bucle while (recorriendo la cadena carácter por carácter).
# =========================================================

palabra = input("Ingresá una palabra: ").lower()
vocales = "aeiou"
contador_vocales = 0
vocales_encontradas = ""
contador_consonantes = 0
consonantes_encontradas = ""
indice = 0

while indice < len(palabra):
    caracter = palabra[indice]
    if caracter in vocales: 
       contador_vocales += 1
       vocales_encontradas +=caracter
    elif caracter.isalpha():
       contador_consonantes += 1
       consonantes_encontradas += caracter
    indice +=1

print(f"hay una cantidad de vocales = {contador_vocales}")
print(f"Las vocales encontradas son: {vocales_encontradas}")
print(f"hay una cantidad de consonantes = {contador_consonantes}")
print(f"Las consonantes encontradas son = {consonantes_encontradas}")