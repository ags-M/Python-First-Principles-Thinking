# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 8
# =========================================================
# CONSIGNA: Pedile al usuario un número mientras NO sea positivo.
# Cuando ingrese uno válido, mostrá "Número aceptado: X"
# =========================================================

# "Pedile un número mientras no sea positivo" = "Pedile un número hasta que sea positivo"
n = int(input("Ingresá un número: "))

while n <= 0:  # mientras sea 0 o negativo, insistí
    print("Número inválido, intentá de nuevo")
    n = int(input("Ingresá un número: "))

print(f"Número aceptado: {n}")