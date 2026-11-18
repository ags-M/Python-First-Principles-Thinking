"""
==========================================================================
Ejercicio 03: Tabla de multiplicar
==========================================================================

ENUNCIADO
---------
Pedile al usuario un entero N. Imprimí su tabla de multiplicar del 1 al 10 usando while (formato: 'N x i = resultado').

PISTA (leela solo si te trabás)
-------------------------------
Mientras i <= 10: imprimí y sumá 1.

"""
n = int(input("Ingresá un número entero: "))
i = 1
while i <= 10:
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    i += 1