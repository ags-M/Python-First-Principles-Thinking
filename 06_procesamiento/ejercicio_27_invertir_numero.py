# ============================================================
# Ejercicio 27: Invertir número
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Dado un número entero, invertí sus dígitos usando while. Ej: 1234 → 4321.
n = int(input("ingresa un numero entero: "))
n_invertido = 0

if n == 0:
    contador_digitos = 1
if n < 0:
    n = -n or abs(n)

while n > 0:
    digito = n % 10
    n_invertido = n_invertido * 10 + digito
    n = n // 10
    

print(f"El numero invertido en: {n_invertido}")


