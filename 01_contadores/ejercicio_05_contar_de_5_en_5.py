# ============================================================
# Ejercicio 5: Contar de 5 en 5
# Categoría: 01_contadores
# ============================================================
#
# ENUNCIADO:
# Mostrá los números 5, 10, 15, 20, ..., 50 usando while.

contador = 5
while contador <= 50:
    print(contador)
    contador += 5
print("Todos son multiplos de 5")
#____________________________________________________________________________________________

# iteracion     valor del contador al entrar     ** se cumple <= 50            que imprime
                                                    #contador <= 50
#___________________________________________________________________________________________

#valor inicial del contador es igual a: 5
#____________________________________________________________________________________________
#     1                      5                       si                         5
#     2                      10                      si                         10
#     3                      15                      si                         15
#     4                      20                      si                         20
#     5                      25                      si                         25
#     6                      30                      si                         30
#     7                      35                      si                         35
#     8                      40                      si                         40
#     9                      45                      si                         45
#    10                      50                      si                         50
#    11                      55                no **: sale del bucle        no imprime nada
#                                              no cumple 55 <= 50
#____________________________________________________________________________________________
