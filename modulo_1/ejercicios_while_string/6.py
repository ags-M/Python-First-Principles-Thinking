# =========================================================
# CONSIGNA: Pedile al usuario una palabra y una letra,
# y contá cuántas veces aparece esa letra en la palabra
# usando un bucle while (recorriendo la cadena carácter
# por carácter).
# ============================================= ============

palabra = input("Ingresá una palabra: ").lower()
letra = input("Ingresá una letra: ").lower()

contador_letra = 0
indice = 0
while indice < len(palabra):
    if letra in palabra[indice]:
        contador_letra += 1
    indice += 1

print(f"Cantidad en la que se repite la letra es: {contador_letra}")

#----------------------------------------------
print("-"*30)
#----------------------------------------------

palabra = input("Ingresá una palabra: ").lower()
letra = input("Ingresá una letra: ").lower()

contador_letra = 0
indice = 0
while indice < len(palabra):
    if letra == palabra[indice]:
        contador_letra += 1
    indice += 1

print(f"La letra '{letra}' aparece {contador_letra} veces en '{palabra}'")
