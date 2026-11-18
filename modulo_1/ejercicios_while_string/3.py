# =========================================================
# CONSIGNA: Pedile al usuario una palabra y mostrala
# invertida (de atrás para adelante) usando un bucle while
# (recorriendo la cadena carácter por carácter).
# =========================================================

palabra = input("Ingresá una palabra: ").lower()  # 1. Pide la palabra al usuario
palabra_invertida = ""                     # 2. Crea una cadena vacía donde guardaremos el resultado
i = len(palabra) - 1                       # 3. 'i' empieza en la última posición (recuerda que los índices 
                                           # van de 0 a len-1)

while i >= 0:                              # 4. Mientras 'i' sea válido (no haya pasado del inicio)
    palabra_invertida += palabra[i]        # 5. Agrega el carácter en posición 'i' a la cadena invertida
    i -= 1                                 # 6. Retrocede una posición

print(f"La palabra invertida es: {palabra_invertida}")