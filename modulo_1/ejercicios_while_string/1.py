# =========================================================
# CONSIGNA: Pedile al usuario una palabra y contá cuántas
# consonantes tiene usando un bucle while (recorriendo la
# cadena carácter por carácter).
# =========================================================

palabra = input("ingresa una palabra: ").lower()
vocales ="aeiou"
contador_consonantes = 0
indice = 0

while indice < len(palabra):
    caracter = palabra[indice]
    if caracter not in vocales:
        contador_consonantes +=1
    indice +=1
print(f"La palabra tiene: {contador_consonantes} consonantes")

#--------------------------------------
print("-"*30)
#--------------------------------------

# CONSIGNA: Pedile al usuario una palabra y contá cuántas vocales tiene
# usando un bucle while (recorriendo la cadena carácter por carácter).
# =========================================================

palabra = input("Ingresá una palabra: ").lower()   # .lower() pasa todo a minúsculas
vocales = "aeiou"
indice = 0
contador_vocales = 0

while indice < len(palabra):  # ¿mientras el índice sea menor que? se pone con < por que arranca de cero!!!
    caracter = palabra[indice] # ¿cómo obtenés la letra en la posición actual?
    if caracter in "vocales": # ¿cómo chequeás si es vocal?
        contador_vocales += 1
    indice += 1  # avanzás al siguiente carácter

print(f"La palabra tiene {contador_vocales} vocales.")