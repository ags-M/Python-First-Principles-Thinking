"""
==========================================================================
Ejercicio 02: Sumar del 1 al N
==========================================================================

ENUNCIADO
---------
Pedile al usuario un entero N >= 1. Calculá la suma 1+2+...+N usando while.

PISTA (leela solo si te trabás)
-------------------------------
Acumulador + contador. Inicializá ambos en 0 y 1.

"""
n = int(input("Ingresá un número N >= 1: "))

i = 1          # contador, arranca en 1
suma = 0       # acumulador, arranca en 0

while i <= n: # condicion
    suma = suma + i    # sumás el valor actual de i
    i += 1             # pasás al siguiente número

print(f"La suma de 1 hasta {n} es: {suma}")

