# ============================================================
# Ejercicio 21: Adivinar número fijo
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# El número secreto es 7. Pedile al usuario que adivine hasta que acierte.
n_secreto = 7
n_usuario = 0
while n_usuario != n_secreto:
    n_usuario =int(input("ingresa un numero: "))
    if n_usuario == n_secreto:
        print("adivinaste")
    else:
        n_usuario =int(input("ingresa un numero: "))

