# ============================================================
# Ejercicio 9: Contar positivos y negativos
# Categoría: 02_acumuladores
# ============================================================
# -----------------------------------------------------------
# ENUNCIADO:
# El usuario ingresa números uno a uno. Cuando ingrese 0, termina.
# Mostrá cuántos positivos y cuántos negativos ingresó.
# yo le agrege que ademas sume los numeros positivos y negativos
# -----------------------------------------------------------

positivos = 0 #contadores
negativos = 0 #contadores
suma_positivos = 0 #acumuladores
suma_negativos = 0 #acumuladores

num = float(input("Ingresá un número (0 para terminar): "))

while num != 0:
    if num > 0:
        suma_positivos = suma_positivos + num
        positivos = positivos + 1
    else:
        suma_negativos = suma_negativos + num
        negativos = negativos + 1

    num = float(input("Ingresá un número (0 para terminar): "))

print(f"ingresaste el numero cero y se cierra el bucle")
print(f"Se ingresaron {positivos} números positivos y suman {suma_positivos} .")
print(f"Se ingresaron {negativos} números negativos y suman {suma_negativos}.")


