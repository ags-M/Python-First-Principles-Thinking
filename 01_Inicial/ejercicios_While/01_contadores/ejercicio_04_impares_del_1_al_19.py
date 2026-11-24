# ============================================================
# Ejercicio 4: Impares del 1 al 19
# Categoría: 01_contadores
# ============================================================
#
# ENUNCIADO:
# Mostrá todos los números impares entre 1 y 19 (inclusive) usando while.

contador = 1 
while contador <= 19:
    print(contador)
    contador += 2
print("Los numeros son impares")


#______________________________________________________________________________________
# iteracion     valor del contador al entrar     ** se cumple <= 19       que imprime
                                                    #contador <= 19
#_________________________________________________________________________________________

#valor inicial del contador es igual a 1
#_______________________________________________________________________________________

#     1                      1                       si                         1
#     2                      3                       si                         3
#     3                      5                       si                         5
#     4                      7                       si                         7
#     5                      9                       si                         9
#     6                     11                       si                         11
#     7                     13                       si                         13
#     8                     15                       si                         15
#     9                     17                       si                         17
#    10                     19                       si                         19
#    11                     20                no **: sale del bucle        no imprime nada 
#                                             no cumple 20 <= 19
# __________________________________________________________________________________  