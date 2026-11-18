"""
==========================================================================
Ejercicio 05: Factorial
==========================================================================

ENUNCIADO
---------
Pedile al usuario N >= 0. Calculá N! usando for.

PISTA (leela solo si te trabás)
-------------------------------
Acumulador multiplicando.

"""
n = int(input("Ingresá un número entero: "))
factorial = 1
for i in range(1, n+1):
   factorial *= i
   print(factorial)
#-------------------------------------------
print("-"* 12)
#-------------------------------------------
n = int(input("Ingresá un número entero: "))
factorial = 1
for i in range(1, n+1):
   factorial *= i
   print(f"factorial parcial {i}! = {factorial}")
print(f"factorial de {n}! = {factorial}")



