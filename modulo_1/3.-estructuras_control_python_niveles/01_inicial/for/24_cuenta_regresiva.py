"""
==========================================================================
Ejercicio 24: Cuenta regresiva
==========================================================================

ENUNCIADO
---------
Pedile al usuario N. Imprimí N, N-1, ..., 1 usando for (con range decreciente).

PISTA (leela solo si te trabás)
-------------------------------
`range(n, 0, -1)`.


"""
n = int(input("Ingresá un número N: "))
for i in range(n, 0, -1): # range(inicio, fin, paso) el fin no incluye el 0 es igual a si n= 4 no incluye el 4 al final
    print(i)


