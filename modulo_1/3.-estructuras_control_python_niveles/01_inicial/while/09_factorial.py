"""
==========================================================================
Ejercicio 09: Factorial
==========================================================================

ENUNCIADO
---------
Pedile al usuario un entero N >= 0. Calculá N! usando while. Recordá: 0! = 1.

PISTA (leela solo si te trabás)
-------------------------------
resultado = 1, multiplicá por 1, 2, ..., N.

"""
n = int(input("Ingresá un número N >= 0: "))
i = 1
resultado = 1  # Empezamos en 1. Si n es 0, el bucle no entra y el resultado queda en 1.

while i <= n:
    resultado = resultado * i  # Acumulamos la multiplicación
    i += 1                     # Avanzamos el contador

print(f"El factorial de {n} es {resultado}")
    