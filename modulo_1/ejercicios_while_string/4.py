# =========================================================
# CONSIGNA: Pedile al usuario una cadena (que puede contener
# letras y números) y contá cuántos caracteres son dígitos
# numéricos usando un bucle while (recorriendo la cadena
# carácter por carácter).
# =========================================================
# Contar dígitos en una cadena
cadena = input("Ingresá una cadena: ")
digitos = "0123456789"
i = 0
contador = 0
while i < len(cadena): # la cadena puede tener una longuitud de 4 pero los indices son 0,1,2,3 por eso i < que len!!!
    if cadena[i] in digitos:
        contador += 1
    i += 1
print(f"La cadena tiene {contador} dígitos.")