# ============================================================
# Ejercicio 28: Número primo
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Pedile un número y decí si es primo usando while. Recordá: primo solo es divisible por 1 y por sí mismo.
#


while True:
    entrada = input("Ingrese un número entero: ")
    try:
        numero = int(entrada)
        break
    except ValueError:
        print("❌ Error: debe ingresar un número entero válido.")