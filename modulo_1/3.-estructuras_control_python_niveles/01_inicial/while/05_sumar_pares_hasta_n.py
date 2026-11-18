"""
==========================================================================
Ejercicio 05: Sumar pares hasta N
==========================================================================

ENUNCIADO
---------
Pedile al usuario N >= 1. Sumá los números pares del 1 al N usando while.

PISTA (leela solo si te trabás)
-------------------------------
Avanzá de a 2 desde el 2, o filtrá con un if.
"""
n = int(input("Ingresá un número N >= 1: "))

i = 1            # arrancamos en 1 (recorremos todos)
suma = 0         # acumulador

while i <= n: # i siempre es el que permite el movimiento y el n es la cantidad un numero
    if i % 2 == 0:        # si i es par
        suma = suma + i   # lo sumamos
    i += 1                # siempre avanzamos al siguiente

print(f"La suma de los pares del 1 al {n} es: {suma}")

#----------------------------------------------
print("-"*12)
#----------------------------------------------

n = int(input("N: "))
i = 1
while i <= n:      # mientras i no supere a n
    print(i)
    i += 1

#----------------------------------------------
print("-"*12)
#----------------------------------------------

n = int(input("N: "))
i = n
while i >= 1:      # mientras i no sea menor que 1
    print(i)
    i -= 1