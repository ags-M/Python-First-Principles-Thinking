# ============================================================
# Ejercicio 28: Número primo
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Pedile un número y decí si es primo usando while. Recordá: primo solo es divisible por 1 y por sí mismo.
#


def contar_digitos_rapido(n):
    return len(str(abs(n)))
print(contar_digitos_rapido(1234))