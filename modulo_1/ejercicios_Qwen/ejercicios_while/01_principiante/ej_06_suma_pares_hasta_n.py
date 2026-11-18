# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 6
# =========================================================
# CONSIGNA: Pedile al usuario un número N y sumá solo los números PARES
# desde 2 hasta N (inclusive si es par).
# =========================================================

n = int(input("Ingresá un número entero positivo: "))
suma_pares = 0
i = 2
while i <= n:
    suma_pares += i
    i += 2
print(f"La suma de los pares hasta {n} es: {suma_pares}")

#--------------------------------------
print("-"*12)
#--------------------------------------

n = int(input("Ingresá un número entero positivo: "))
i = 2
suma = 0
while i <= n:
    if i % 2 == 0: # i es el contador que va subiendo (2, 4, 6, 8...). Ese es el que hay que chequear.
       suma += i # lo que acumula es el contador ...n solo dice cuantas veces lo hace
    i += 1 # siempre actualiza fuera del if
print(f"La suma de los n pares hasta {n}: {suma}")





