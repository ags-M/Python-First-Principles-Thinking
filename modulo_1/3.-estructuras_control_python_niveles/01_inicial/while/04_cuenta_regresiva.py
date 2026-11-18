"""
==========================================================================
Ejercicio 04: Cuenta regresiva
==========================================================================

ENUNCIADO
---------
Pedile al usuario un entero N >= 1. Imprimí los números de N hasta 1 usando while.

PISTA (leela solo si te trabás)
-------------------------------
Empezá con i = N y restá 1 en cada vuelta.
"""
n = int(input("Ingresá un número N >= 1: "))
i = n
while i >= 1:
    print(i)
    i -= 1