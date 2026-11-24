# ============================================================
# Ejercicio 3: Pares del 2 al 20
# Categoría: 01_contadores
# ============================================================
#
# ENUNCIADO:
# Mostrá todos los números pares entre 2 y 20 (inclusive) usando while.

contador = 2
while contador <= 20:
       print(contador)
       contador += 2
print("final son todos pares")

#______________________________________________________________________________________

# iteracion     valor del contador al entrar     ** se cumple <= 20            que imprime
                                                    #contador <= 20
#_________________________________________________________________________________________

#valor inicial del contador es igual a 2
#_______________________________________________________________________________________

#     1                      2                       si                         2
#     2                      4                       si                         4
#     3                      6                       si                         6
#     4                      8                       si                         8
#     5                     10                       si                         10
#     6                     12                       si                         12
#     7                     14                       si                         14             
#     8                     16                       si                         16
#     9                     18                       si                         18
#    10                     20                       si                         20
#    11                     22            no **: sale del bucle         no imprime nada
#                                         no cumple 22 <= 20
#_______________________________________________________________________________________



