# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 5
# =========================================================
# CONSIGNA: Pedile al usuario un número N y calculá la suma de todos los números
# desde 1 hasta N. Mostrá el resultado.
# Ejemplo: si N = 5 → 1+2+3+4+5 = 15
# =========================================================

n = int(input("Ingresá un número entero positivo: "))
suma = 0
i = 1 # (acumulador) e i = 1 (contador que arranca en 1)
while i <= n: # el bucle se ejecuta mientras i no haya pasado el techo
    suma += i #  suma el valor actual de i al acumulador
    i += 1 # sube de a 1, así el bucle eventualmente termina
print(f"La suma desde 1 hasta {n} es: {suma}")


     