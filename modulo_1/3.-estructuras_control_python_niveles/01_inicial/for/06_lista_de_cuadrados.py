"""
==========================================================================
Ejercicio 06: Lista de cuadrados
==========================================================================

ENUNCIADO
---------
Pedile al usuario N >= 1. Mostrá una lista con los cuadrados de 1 a N usando for.

PISTA (leela solo si te trabás)
-------------------------------
`i*i` para cada i.

"""
n = int(input("Ingresá un número N >= 1: "))
suma = 0
for i in range(1, n+1):
    cuadrados = i*i
    print(f"el cuadrado de {i} es: {cuadrados}")
    suma = suma + cuadrados
print(f"la suma de todos los cuadrados de 1 a {n} es igual a {suma}")



