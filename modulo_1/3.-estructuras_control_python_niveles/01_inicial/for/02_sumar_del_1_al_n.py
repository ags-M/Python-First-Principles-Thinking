"""
==========================================================================
Ejercicio 02: Sumar del 1 al N
==========================================================================

ENUNCIADO
---------
Pedile al usuario N >= 1. Calculá 1+2+...+N usando for.

PISTA (leela solo si te trabás)
-------------------------------
Acumulador con `range(1, n+1)`.

"""
n = int(input("Ingresá un número N >= 1: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de 1 hasta {n} es: {suma}")
#----------------------------------------------
print("-"*12)
#----------------------------------------------
n = int(input("Ingresá un número N >= 1: "))
for i in range(0, n + 1):
    print(i)
#----------------------------------------------
print("-"*12)
#----------------------------------------------
n = int(input("Ingresá un número N >= 1: "))
for i in range(n, -1, -1): # range(inicio, fin, paso)
    print(i)



