# ============================================================
# Ejercicio 32: Triángulo de N filas
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Igual que el anterior, pero pedile al usuario cuántas filas quiere.

filas = int(input("ingresa el numero de filas que deseas para realizar un triangulo recto: "))

i = 1

while i <= filas:
    asteriscos = ""
    j = 1
    while j <= i:
        asteriscos += "*"
        j += 1
    print(asteriscos)
    i += 1
