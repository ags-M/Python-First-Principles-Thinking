# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 11
# =========================================================
# CONSIGNA: Pedile al usuario un número entero y contá cuántos dígitos tiene
# usando solo while (sin convertir a string).
# PISTA: dividí por 10 mientras sea mayor a 0.
# =========================================================

numero = int(input("Ingresá un número entero: "))
contador = 0 # ¿en qué número debe empezar el contador?

while numero > 0 : # ¿cuándo debe seguir el bucle?
    contador = contador +1 # ¿qué le sumamos al contador?
    numero = numero // 10  # ¿qué operación le hacemos al número?
print(f"El número tiene {contador} dígitos")