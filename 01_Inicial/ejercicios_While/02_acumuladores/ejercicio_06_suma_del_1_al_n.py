# ============================================================
# Ejercicio 6: Suma del 1 al N
# Categoría: 02_acumuladores
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario un número N y calculá la suma de todos los números desde 1 hasta N usando while.
#
n = int(input("ingrese un numero: "))
suma = 0
contador = 1
while contador <= n:
    suma = suma + contador
    contador += 1
print(f"La suma de 1 a {n} es: {suma}")

#____________________________________________________________________________________________

# iteracion     valor del contador al entrar   **se cumple <= 10      que imprime
#____________________________________________________________________________________________
#valor inicial del contador es igual a: 1                                 suma + contador
#____________________________________________________________________________________________
#     1                      1                       si                         1
#     2                      2                       si                         3
#     3                      3                       si                         6
#     4                      4                       si                         10
#     5                      5                       si                         15
#     6                      6                       si                         21
#     7                      7                       si                         28
#     8                      8                       si                         36
#     9                      9                       si                         45
#    10                     10                       si                         55
#    11                     11                no **: sale del bucle        no imprime nada
#                                             no cumple 11 <= 10
#____________________________________________________________________________________________