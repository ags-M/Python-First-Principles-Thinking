# ============================================================
# Ejercicio 1: Contar del 1 al 10
# Categoría: 01_contadores
# ============================================================
#
# ENUNCIADO:
# Usando un bucle while, mostrá en pantalla los números del 1 al 10, uno por línea.
#
# -----------------------------------------------------------
# PISTA para principiantes:
# Recordá la estructura básica del while:
#
#   variable = valor_inicial
#   while condicion:
#       # acciones
#       variable = variable + 1   (o lo que corresponda)
#
# Escribí tu solución debajo de esta línea.
# Cuando termines, probá el programa con varios casos.
# -----------------------------------------------------------
contador = 1 # inicio
while contador <= 10: #condicion
    print(contador) # cuerpo: que es lo que hará imprimiendo la salida del traceo
    contador += 1 # actualizo
print("El contador terminó") # imprimo el final 

#______________________________________________________________________________________

# iteracion    valor del contador al entrar    ** se cumple <= 10   que imprime
#                                                  contador <= 10
#______________________________________________________________________________________

#valor inicial del contador es igual a 1
#_______________________________________________________________________________________

#     1                      1                       si                         1
#     2                      2                       si                         2
#     3                      3                       si                         3
#     4                      4                       si                         4
#     5                      5                       si                         5
#     6                      6                       si                         6
#     7                      7                       si                         7
#     8                      8                       si                         8
#     9                      9                       si                         9
#    10                      10                      si                        10
#    11                      11            no **: sale del bucle        no imprime nada
#                                             no cumple 11 <=10
#_____________________________________________________________________________________
    


