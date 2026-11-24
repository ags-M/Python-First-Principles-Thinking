# ============================================================
# Ejercicio 27: Invertir número
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Dado un número entero, invertí sus dígitos usando while. Ej: 1234 → 4321.
n = int(input("ingresa un numero entero: "))

es_n_negativo = n < 0 # hay que tener en cuenta el ingreso de un numero negativo
n = abs(n) # se puede escribir = -n es lo mismo que el absoluto, lo convertimos para poder manejar los digitos
n_invertido = 0


while n > 0:
    digito = n % 10
    n_invertido = n_invertido * 10 + digito
    n = n // 10

# Restauramos el signo si el numero ingresado por el usuario era negativo
if es_n_negativo:
    n_invertido = - n_invertido   

print(f"El numero invertido es: {n_invertido}")


