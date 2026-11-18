# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 10
# =========================================================
# CONSIGNA: Pedile al usuario una palabra y contá cuántas vocales tiene
# usando un bucle while (recorriendo la cadena carácter por carácter).
# =========================================================

palabra = input("Ingresá una palabra: ").lower()   # .lower() pasa todo a minúsculas
vocales = "aeiou"
indice = 0
contador_vocales = 0

while indice < len(palabra):  # ¿mientras el índice sea menor que? se pone con < por que arranca de cero!!!
    caracter = palabra[indice] # ¿cómo obtenés la letra en la posición actual?
    if caracter in vocales: # ¿cómo chequeás si es vocal?
        contador_vocales += 1
    indice += 1  # avanzás al siguiente carácter

print(f"La palabra tiene {contador_vocales} vocales.")

#--------------------------------------
print("-"*12)
#--------------------------------------

palabra = "hola" 
# En Python, una cadena de texto es como una fila de cajitas, 
#donde cada cajita tiene una letra y un número de posición (llamado "índice").
# Por eso cada CARACTER de la palabra tiene un indice
print(palabra[0]) # Con la sintaxis palabra[indice]: como empieza con 0 es = cantidad de letras -1
print(palabra[1])
print(palabra[2])
print(palabra[3])

#--------------------------------------
print("-"*12)
#--------------------------------------

#pero que longuitud tiene la palabra?
palabra = "python"
print(f"La palabra {palabra} tiene una longuitud de: {len(palabra)} caracteres")# imprime 6, 
#pero ojo!! Entonces los índices válidos van de 0 a len(palabra) - 1, o sea de 0 a 5.

